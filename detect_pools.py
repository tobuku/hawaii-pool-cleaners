#!/usr/bin/env python3
"""
detect_pools.py
Step 3: Color-heuristic pool detection over downloaded satellite tiles.

Pool water in Esri World Imagery appears as aqua/blue (HSV H≈170–210°, S≈40–100%, V≈40–90%).
Connected regions of qualifying pixels are converted to lat/lon centroids.

Usage:
  python detect_pools.py           # process all downloaded tiles
  python detect_pools.py --test    # process tiles for Kahala/Hawaii Kai only (quick sanity check)

Requires: pip install pillow numpy scipy
Output: pool-data/detections.json
"""

import os
import json
import math
import argparse
import glob

import numpy as np
from PIL import Image
from scipy import ndimage

TILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pool-data", "tiles")
OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pool-data", "detections.json")
ZOOM = 17
TILE_PX = 256  # Esri tiles are 256×256

# HSV thresholds for pool water (H in 0-360 range, S/V in 0-100 range)
H_MIN, H_MAX = 170, 215   # aqua to blue
S_MIN, S_MAX = 35, 100
V_MIN, V_MAX = 35, 92

# Region area filters (pixels)
MIN_PX = 25
MAX_PX = 4000

# Test mode bbox: Kahala + Hawaii Kai (many private pools)
TEST_BBOX = (21.27, -157.78, 21.32, -157.67)


# ---------------------------------------------------------------------------
# Tile math
# ---------------------------------------------------------------------------

def deg2tile(lat_deg, lon_deg, zoom):
    lat_r = math.radians(lat_deg)
    n = 2 ** zoom
    x = int((lon_deg + 180.0) / 360.0 * n)
    y = int((1.0 - math.asinh(math.tan(lat_r)) / math.pi) / 2.0 * n)
    return x, y


def tile2deg(x, y, zoom):
    """Return (lat, lon) of the NW corner of tile (x, y) at zoom."""
    n = 2 ** zoom
    lon = x / n * 360.0 - 180.0
    lat_r = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
    lat = math.degrees(lat_r)
    return lat, lon


def pixel_to_latlon(tile_x, tile_y, px_col, px_row, zoom):
    """Convert a pixel within a tile to lat/lon."""
    # Fractional tile coords
    tile_fx = tile_x + px_col / TILE_PX
    tile_fy = tile_y + px_row / TILE_PX
    lat, lon = tile2deg(tile_fx, tile_fy, zoom)
    return lat, lon


# ---------------------------------------------------------------------------
# Detection
# ---------------------------------------------------------------------------

def rgb_to_hsv_array(img_array):
    """Convert RGB uint8 array (H,W,3) to HSV with H in [0,360], S/V in [0,100]."""
    r = img_array[:, :, 0].astype(np.float32) / 255.0
    g = img_array[:, :, 1].astype(np.float32) / 255.0
    b = img_array[:, :, 2].astype(np.float32) / 255.0

    cmax = np.maximum(np.maximum(r, g), b)
    cmin = np.minimum(np.minimum(r, g), b)
    delta = cmax - cmin

    # Hue
    h = np.zeros_like(r)
    mask_r = (cmax == r) & (delta > 0)
    mask_g = (cmax == g) & (delta > 0)
    mask_b = (cmax == b) & (delta > 0)
    h[mask_r] = (60 * ((g[mask_r] - b[mask_r]) / delta[mask_r])) % 360
    h[mask_g] = 60 * ((b[mask_g] - r[mask_g]) / delta[mask_g] + 2)
    h[mask_b] = 60 * ((r[mask_b] - g[mask_b]) / delta[mask_b] + 4)

    # Saturation
    s = np.where(cmax > 0, delta / cmax * 100, 0)

    # Value
    v = cmax * 100

    return h, s, v


def detect_in_tile(tile_x, tile_y, img_array):
    """Return list of (lat, lon) for detected pool centroids in this tile."""
    h, s, v = rgb_to_hsv_array(img_array)

    mask = (
        (h >= H_MIN) & (h <= H_MAX) &
        (s >= S_MIN) & (s <= S_MAX) &
        (v >= V_MIN) & (v <= V_MAX)
    )

    labeled, num_features = ndimage.label(mask)
    if num_features == 0:
        return []

    detections = []
    for label_id in range(1, num_features + 1):
        region = labeled == label_id
        area = region.sum()
        if area < MIN_PX or area > MAX_PX:
            continue
        # Centroid in pixel coords
        rows, cols = np.where(region)
        px_row = int(rows.mean())
        px_col = int(cols.mean())
        lat, lon = pixel_to_latlon(tile_x, tile_y, px_col, px_row, ZOOM)
        detections.append({"lat": round(lat, 6), "lon": round(lon, 6), "px": int(area)})

    return detections


def get_tile_files(test_mode=False):
    """Return list of tile paths. In test mode, restrict to test bbox."""
    pattern = os.path.join(TILES_DIR, str(ZOOM), "**", "*.jpg")
    all_files = glob.glob(pattern, recursive=True)

    if not test_mode:
        return all_files

    # Filter to test bbox tile range
    s, w, n, e = TEST_BBOX
    x_min, y_max = deg2tile(s, w, ZOOM)
    x_max, y_min = deg2tile(n, e, ZOOM)
    filtered = []
    for f in all_files:
        parts = f.replace("\\", "/").split("/")
        try:
            tile_x = int(parts[-2])
            tile_y = int(os.path.splitext(parts[-1])[0])
            if x_min <= tile_x <= x_max and y_min <= tile_y <= y_max:
                filtered.append(f)
        except (ValueError, IndexError):
            pass
    return filtered


def parse_tile_path(path):
    """Extract (x, y) from pool-data/tiles/17/x/y.jpg"""
    parts = path.replace("\\", "/").split("/")
    tile_x = int(parts[-2])
    tile_y = int(os.path.splitext(parts[-1])[0])
    return tile_x, tile_y


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true",
                        help="Run on Kahala/Hawaii Kai tiles only (quick sanity check)")
    args = parser.parse_args()

    tile_files = get_tile_files(test_mode=args.test)
    if not tile_files:
        print(f"No tiles found in {TILES_DIR}. Run tile_downloader.py first.")
        return

    print(f"Processing {len(tile_files)} tiles...")
    if args.test:
        print("(Test mode: Kahala/Hawaii Kai area)")

    all_detections = []
    no_detect = 0

    for i, path in enumerate(tile_files, 1):
        try:
            tile_x, tile_y = parse_tile_path(path)
            img = Image.open(path).convert("RGB")
            arr = np.array(img)
            hits = detect_in_tile(tile_x, tile_y, arr)
            if hits:
                all_detections.extend(hits)
            else:
                no_detect += 1
        except Exception as e:
            print(f"  WARN {path}: {e}")
            continue

        if i % 1000 == 0 or i == len(tile_files):
            print(f"  [{i}/{len(tile_files)}] detections so far: {len(all_detections)}")

    print(f"\nTiles with detections: {len(tile_files) - no_detect}")
    print(f"Tiles with no detections: {no_detect}")
    print(f"Total raw detections: {len(all_detections)}")

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(all_detections, f, indent=2)
    print(f"Wrote {len(all_detections)} detections -> {OUT_PATH}")


if __name__ == "__main__":
    main()
