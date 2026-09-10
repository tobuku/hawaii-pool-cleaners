#!/usr/bin/env python3
"""
merge_pools.py
Step 4: Merge OSM pool data + CV detections into the final lead list.

- Deduplicates: any two points within 20m → keep OSM entry
- Reverse geocodes CV-only detections via Nominatim (1 req/sec)
- Assigns neighborhood slug via bbox lookup
- Writes pool-data/all_pools.geojson and pool-data/all_pools.csv

Usage: python merge_pools.py
"""

import json
import csv
import os
import math
import time
import requests

NOMINATIM_URL = "https://nominatim.openstreetmap.org/reverse"
NOMINATIM_HEADERS = {"User-Agent": "HawaiiPoolCleaner-LeadGen/1.0 (neal@hawaiipoolcleaners.com)"}

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pool-data")
OSM_GEOJSON = os.path.join(OUT_DIR, "osm_pools.geojson")
DETECTIONS_JSON = os.path.join(OUT_DIR, "detections.json")
OUT_GEOJSON = os.path.join(OUT_DIR, "all_pools.geojson")
OUT_CSV = os.path.join(OUT_DIR, "all_pools.csv")

DEDUP_METERS = 20  # merge radius

NEIGHBORHOOD_BBOXES = {
    "honolulu":                   (21.28, -157.87, 21.34, -157.80),
    "kailua":                     (21.37, -157.76, 21.42, -157.70),
    "kaneohe":                    (21.38, -157.82, 21.44, -157.78),
    "kapolei":                    (21.32, -158.10, 21.37, -158.04),
    "mililani":                   (21.44, -158.03, 21.49, -157.98),
    "pearl-city":                 (21.38, -157.98, 21.42, -157.93),
    "hawaii-kai":                 (21.28, -157.71, 21.32, -157.67),
    "aiea":                       (21.37, -157.94, 21.41, -157.90),
    "waipahu":                    (21.37, -158.02, 21.41, -157.97),
    "ewa-beach":                  (21.30, -158.05, 21.34, -157.99),
    "ewa-gentry":                 (21.33, -158.07, 21.37, -158.01),
    "waikiki":                    (21.27, -157.84, 21.30, -157.81),
    "kaimuki":                    (21.28, -157.80, 21.31, -157.77),
    "manoa":                      (21.29, -157.82, 21.33, -157.79),
    "salt-lake":                  (21.35, -157.92, 21.38, -157.89),
    "aliamanu":                   (21.36, -157.91, 21.39, -157.88),
    "moanalua":                   (21.36, -157.90, 21.39, -157.87),
    "pearl-harbor":               (21.35, -157.96, 21.39, -157.92),
    "downtown-honolulu":          (21.30, -157.87, 21.32, -157.84),
    "kakaako":                    (21.29, -157.87, 21.31, -157.85),
    "ala-moana":                  (21.28, -157.85, 21.30, -157.83),
    "kapahulu":                   (21.28, -157.81, 21.30, -157.79),
    "mccully":                    (21.29, -157.83, 21.31, -157.81),
    "kalihi":                     (21.32, -157.89, 21.36, -157.85),
    "punchbowl":                  (21.30, -157.86, 21.32, -157.83),
    "palolo":                     (21.28, -157.79, 21.31, -157.76),
    "aina-haina":                 (21.28, -157.74, 21.31, -157.72),
    "niu-valley":                 (21.28, -157.72, 21.30, -157.70),
    "kalama-valley":              (21.29, -157.70, 21.31, -157.68),
    "kahala":                     (21.27, -157.78, 21.30, -157.75),
    "enchanted-lake":             (21.38, -157.74, 21.41, -157.71),
    "lanikai":                    (21.38, -157.72, 21.41, -157.69),
    "waimanalo":                  (21.32, -157.73, 21.37, -157.69),
    "kaneohe-bay":                (21.44, -157.83, 21.48, -157.78),
    "ahuimanu":                   (21.43, -157.83, 21.46, -157.80),
    "makakilo":                   (21.35, -158.10, 21.38, -158.06),
    "iroquois-point":             (21.32, -157.99, 21.35, -157.96),
    "hickam-housing":             (21.33, -157.96, 21.36, -157.93),
    "schofield-barracks":         (21.48, -158.07, 21.52, -158.02),
    "wheeler-army-airfield":      (21.47, -158.05, 21.50, -158.01),
    "tripler-army-medical-center":(21.36, -157.88, 21.38, -157.86),
    "haleiwa":                    (21.58, -158.12, 21.62, -158.08),
    "waialua":                    (21.56, -158.14, 21.60, -158.10),
    "kahuku":                     (21.67, -157.96, 21.72, -157.92),
    "laie":                       (21.64, -157.93, 21.68, -157.89),
    "hauula":                     (21.60, -157.92, 21.63, -157.88),
    "kaaawa":                     (21.55, -157.86, 21.58, -157.82),
    "waianae":                    (21.44, -158.20, 21.48, -158.16),
    "nanakuli":                   (21.38, -158.17, 21.42, -158.13),
    "maili":                      (21.41, -158.19, 21.44, -158.15),
    "makaha":                     (21.46, -158.24, 21.50, -158.20),
    "whitmore-village":           (21.51, -158.06, 21.54, -158.02),
    "campbell-industrial-park":   (21.31, -158.08, 21.34, -158.04),
}


def assign_neighborhood(lat, lon):
    for slug, (s, w, n, e) in NEIGHBORHOOD_BBOXES.items():
        if s <= lat <= n and w <= lon <= e:
            return slug
    return "unknown"


def haversine_meters(lat1, lon1, lat2, lon2):
    """Approximate distance in meters between two lat/lon points."""
    R = 6_371_000
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def reverse_geocode(lat, lon):
    try:
        resp = requests.get(
            NOMINATIM_URL,
            params={"format": "json", "lat": lat, "lon": lon, "zoom": 18},
            headers=NOMINATIM_HEADERS,
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json().get("display_name", "")
    except Exception as e:
        print(f"  Nominatim error ({lat},{lon}): {e}")
        return ""


def load_osm(path):
    if not os.path.exists(path):
        print(f"OSM file not found: {path} — skipping OSM data.")
        return []
    with open(path, encoding="utf-8") as f:
        gj = json.load(f)
    pools = []
    for feat in gj.get("features", []):
        p = feat["properties"]
        pools.append({
            "id": p.get("id", ""),
            "lat": p["lat"],
            "lon": p["lon"],
            "name": p.get("name", ""),
            "address": p.get("address", ""),
            "neighborhood": p.get("neighborhood", "unknown"),
            "source": "osm",
        })
    return pools


def load_detections(path):
    if not os.path.exists(path):
        print(f"Detections file not found: {path} — skipping CV data.")
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def is_duplicate(lat, lon, existing_pools):
    """True if any existing pool is within DEDUP_METERS."""
    for p in existing_pools:
        if haversine_meters(lat, lon, p["lat"], p["lon"]) <= DEDUP_METERS:
            return True
    return False


def main():
    print("Loading OSM pools...")
    osm_pools = load_osm(OSM_GEOJSON)
    print(f"  {len(osm_pools)} OSM pools loaded.")

    print("Loading CV detections...")
    detections = load_detections(DETECTIONS_JSON)
    print(f"  {len(detections)} raw CV detections loaded.")

    # Start with all OSM pools
    merged = list(osm_pools)

    # Add CV detections that are not duplicates of OSM
    print("\nDeduplicating CV detections against OSM pools...")
    new_cv = 0
    dup_cv = 0
    geocode_needed = []

    for det in detections:
        lat, lon = det["lat"], det["lon"]
        if is_duplicate(lat, lon, merged):
            dup_cv += 1
        else:
            geocode_needed.append(det)

    print(f"  Duplicates (suppressed): {dup_cv}")
    print(f"  New CV detections to geocode: {len(geocode_needed)}")

    for i, det in enumerate(geocode_needed, 1):
        lat, lon = det["lat"], det["lon"]
        print(f"  Geocoding CV [{i}/{len(geocode_needed)}] ({lat},{lon})")
        address = reverse_geocode(lat, lon)
        time.sleep(1.0)
        neighborhood = assign_neighborhood(lat, lon)
        merged.append({
            "id": f"cv-{i}",
            "lat": lat,
            "lon": lon,
            "name": "",
            "address": address,
            "neighborhood": neighborhood,
            "source": "cv",
        })
        new_cv += 1

    print(f"\nMerge complete:")
    print(f"  OSM pools:       {len(osm_pools)}")
    print(f"  New CV pools:    {new_cv}")
    print(f"  Total:           {len(merged)}")

    # Write GeoJSON
    features = []
    for pool in merged:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [pool["lon"], pool["lat"]],
            },
            "properties": pool,
        })
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_GEOJSON, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": features}, f, indent=2)
    print(f"Wrote -> {OUT_GEOJSON}")

    # Write CSV
    fieldnames = ["id", "lat", "lon", "name", "address", "neighborhood", "source"]
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(merged)
    print(f"Wrote -> {OUT_CSV}")


if __name__ == "__main__":
    main()
