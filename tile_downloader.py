#!/usr/bin/env python3
"""
tile_downloader.py
Step 2: Download Esri World Imagery satellite tiles at zoom 17 for Oahu.

Usage:
  python tile_downloader.py                # all priority neighborhoods
  python tile_downloader.py --priority-only  # same (default)
  python tile_downloader.py --all          # full Oahu bbox (much larger, ~135k tiles)

Tiles saved to: pool-data/tiles/{z}/{x}/{y}.jpg
Rate: 4 workers, ~2 req/sec per worker (polite).
Runtime estimate: ~4 hours for priority areas (~30k tiles).
"""

import os
import math
import time
import argparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

ZOOM = 17
TILE_URL = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"

TILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pool-data", "tiles")
os.makedirs(TILES_DIR, exist_ok=True)

# Full Oahu bbox
OAHU_BBOX = dict(south=21.25, west=-158.32, north=21.72, east=-157.65)

# Priority neighborhoods (slug: (south, west, north, east))
PRIORITY_BBOXES = {
    "honolulu":    (21.28, -157.87, 21.34, -157.80),
    "kailua":      (21.37, -157.76, 21.42, -157.70),
    "kaneohe":     (21.38, -157.82, 21.44, -157.78),
    "hawaii-kai":  (21.28, -157.71, 21.32, -157.67),
    "kapolei":     (21.32, -158.10, 21.37, -158.04),
    "mililani":    (21.44, -158.03, 21.49, -157.98),
    "pearl-city":  (21.38, -157.98, 21.42, -157.93),
    "aiea":        (21.37, -157.94, 21.41, -157.90),
    "waipahu":     (21.37, -158.02, 21.41, -157.97),
    "ewa-beach":   (21.30, -158.05, 21.34, -157.99),
}

WORKERS = 4
REQUEST_DELAY = 0.5  # seconds between requests per worker (2 req/sec)
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "HawaiiPoolCleaner-LeadGen/1.0"})


# ---------------------------------------------------------------------------
# Slippy map tile math
# ---------------------------------------------------------------------------

def deg2tile(lat_deg, lon_deg, zoom):
    """Convert lat/lon to tile x, y at zoom level."""
    lat_r = math.radians(lat_deg)
    n = 2 ** zoom
    x = int((lon_deg + 180.0) / 360.0 * n)
    y = int((1.0 - math.asinh(math.tan(lat_r)) / math.pi) / 2.0 * n)
    return x, y


def bbox_to_tile_range(south, west, north, east, zoom):
    """Return (x_min, x_max, y_min, y_max) tile range for a bbox."""
    x_min, y_max = deg2tile(south, west, zoom)  # south-west = high y
    x_max, y_min = deg2tile(north, east, zoom)  # north-east = low y
    return x_min, x_max, y_min, y_max


def tile_path(z, x, y):
    return os.path.join(TILES_DIR, str(z), str(x), str(y) + ".jpg")


def collect_tiles(bboxes):
    """Build a deduplicated list of (z, x, y) tuples from a dict of bboxes."""
    tile_set = set()
    for slug, (s, w, n, e) in bboxes.items():
        x_min, x_max, y_min, y_max = bbox_to_tile_range(s, w, n, e, ZOOM)
        count = (x_max - x_min + 1) * (y_max - y_min + 1)
        print(f"  {slug:30s} {count:6d} tiles  x=[{x_min},{x_max}] y=[{y_min},{y_max}]")
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                tile_set.add((ZOOM, x, y))
    return list(tile_set)


def download_tile(args):
    """Download a single tile. Returns (z,x,y,'ok'|'skip'|'error')."""
    z, x, y = args
    path = tile_path(z, x, y)
    if os.path.exists(path):
        return z, x, y, "skip"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    url = TILE_URL.format(z=z, y=y, x=x)
    try:
        time.sleep(REQUEST_DELAY)
        resp = SESSION.get(url, timeout=15)
        if resp.status_code == 200 and len(resp.content) > 500:
            with open(path, "wb") as f:
                f.write(resp.content)
            return z, x, y, "ok"
        else:
            return z, x, y, f"http{resp.status_code}"
    except Exception as e:
        return z, x, y, f"error:{e}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Download full Oahu bbox")
    parser.add_argument("--priority-only", action="store_true", default=True,
                        help="Download priority neighborhoods only (default)")
    args = parser.parse_args()

    if args.all:
        bboxes = {"oahu-full": (
            OAHU_BBOX["south"], OAHU_BBOX["west"],
            OAHU_BBOX["north"], OAHU_BBOX["east"]
        )}
        print("Mode: full Oahu (~135,000 tiles)")
    else:
        bboxes = PRIORITY_BBOXES
        print("Mode: priority neighborhoods (~30,000 tiles)")

    print("\nCalculating tile ranges...")
    tiles = collect_tiles(bboxes)

    already_done = sum(1 for z, x, y in tiles if os.path.exists(tile_path(z, x, y)))
    to_download = len(tiles) - already_done
    print(f"\nTotal unique tiles: {len(tiles)}")
    print(f"Already on disk:    {already_done}")
    print(f"To download:        {to_download}")
    if to_download == 0:
        print("Nothing to download.")
        return

    print(f"\nStarting download with {WORKERS} workers...")
    ok = skip = errors = 0
    start = time.time()

    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        futures = {executor.submit(download_tile, t): t for t in tiles}
        for i, future in enumerate(as_completed(futures), 1):
            z, x, y, status = future.result()
            if status == "ok":
                ok += 1
            elif status == "skip":
                skip += 1
            else:
                errors += 1
                print(f"  WARN {z}/{x}/{y}: {status}")

            if i % 500 == 0 or i == len(tiles):
                elapsed = time.time() - start
                rate = ok / elapsed if elapsed > 0 else 0
                eta = (to_download - ok) / rate if rate > 0 else 0
                print(f"  [{i}/{len(tiles)}] ok={ok} skip={skip} err={errors} "
                      f"rate={rate:.1f}/s ETA={eta/60:.0f}min")

    elapsed = time.time() - start
    print(f"\nDone. Downloaded {ok} tiles, skipped {skip}, errors {errors}.")
    print(f"Elapsed: {elapsed/60:.1f} minutes")
    print(f"Tiles stored in: {TILES_DIR}")


if __name__ == "__main__":
    main()
