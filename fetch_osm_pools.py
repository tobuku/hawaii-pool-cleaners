#!/usr/bin/env python3
"""
fetch_osm_pools.py
Step 1: Query Overpass API for swimming pools on Oahu, reverse geocode each,
assign neighborhood, and write pool-data/osm_pools.geojson + osm_pools.csv.

Usage: python fetch_osm_pools.py
"""

import json
import time
import csv
import os
import requests

# ---------------------------------------------------------------------------
# Oahu bounding box
# ---------------------------------------------------------------------------
BBOX = dict(south=21.25, west=-158.32, north=21.72, east=-157.65)

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
NOMINATIM_URL = "https://nominatim.openstreetmap.org/reverse"
NOMINATIM_HEADERS = {"User-Agent": "HawaiiPoolCleaner-LeadGen/1.0 (neal@hawaiipoolcleaners.com)"}

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pool-data")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Neighborhood bounding boxes  (south, west, north, east)
# Approximate rectangles — good enough for slug assignment.
# ---------------------------------------------------------------------------
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
    """Return slug of the first matching bounding box, or 'unknown'."""
    for slug, (s, w, n, e) in NEIGHBORHOOD_BBOXES.items():
        if s <= lat <= n and w <= lon <= e:
            return slug
    return "unknown"


def overpass_query():
    """Fetch all swimming pool nodes/ways from Overpass."""
    query = (
        "[out:json][timeout:90];\n"
        "(\n"
        f"  node[leisure=swimming_pool]({BBOX['south']},{BBOX['west']},{BBOX['north']},{BBOX['east']});\n"
        f"  way[leisure=swimming_pool]({BBOX['south']},{BBOX['west']},{BBOX['north']},{BBOX['east']});\n"
        f"  node[amenity=swimming_pool]({BBOX['south']},{BBOX['west']},{BBOX['north']},{BBOX['east']});\n"
        "  way[amenity=swimming_pool]"
        f"({BBOX['south']},{BBOX['west']},{BBOX['north']},{BBOX['east']});\n"
        ");\n"
        "out center;"
    )
    print("Querying Overpass API...")
    headers = {"User-Agent": "HawaiiPoolCleaner-LeadGen/1.0 (neal@hawaiipoolcleaners.com)"}
    resp = requests.post(OVERPASS_URL, data={"data": query}, headers=headers, timeout=120)
    resp.raise_for_status()
    return resp.json()


def extract_coords(element):
    """Return (lat, lon) from a node or way-with-center."""
    if element["type"] == "node":
        return element["lat"], element["lon"]
    if element["type"] == "way" and "center" in element:
        return element["center"]["lat"], element["center"]["lon"]
    return None, None


def reverse_geocode(lat, lon):
    """Call Nominatim reverse geocode; return display_name or empty string."""
    try:
        resp = requests.get(
            NOMINATIM_URL,
            params={"format": "json", "lat": lat, "lon": lon, "zoom": 18},
            headers=NOMINATIM_HEADERS,
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("display_name", "")
    except Exception as e:
        print(f"  Nominatim error for ({lat},{lon}): {e}")
        return ""


def main():
    data = overpass_query()
    elements = data.get("elements", [])
    print(f"Overpass returned {len(elements)} elements.")

    features = []
    rows = []

    for i, el in enumerate(elements):
        lat, lon = extract_coords(el)
        if lat is None:
            continue

        tags = el.get("tags", {})
        name = tags.get("name", "")

        print(f"  [{i+1}/{len(elements)}] ({lat:.5f}, {lon:.5f}) {name}")

        address = reverse_geocode(lat, lon)
        time.sleep(1.0)  # Nominatim rate-limit: 1 req/sec

        neighborhood = assign_neighborhood(lat, lon)

        feature = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [lon, lat]},
            "properties": {
                "id": f"osm-{el['id']}",
                "lat": lat,
                "lon": lon,
                "name": name,
                "address": address,
                "neighborhood": neighborhood,
                "source": "osm",
                "osm_id": el["id"],
                "osm_type": el["type"],
            },
        }
        features.append(feature)

        rows.append({
            "id": f"osm-{el['id']}",
            "lat": lat,
            "lon": lon,
            "name": name,
            "address": address,
            "neighborhood": neighborhood,
            "source": "osm",
        })

    # Write GeoJSON
    geojson_path = os.path.join(OUT_DIR, "osm_pools.geojson")
    with open(geojson_path, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": features}, f, indent=2)
    print(f"\nWrote {len(features)} features -> {geojson_path}")

    # Write CSV
    csv_path = os.path.join(OUT_DIR, "osm_pools.csv")
    fieldnames = ["id", "lat", "lon", "name", "address", "neighborhood", "source"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows -> {csv_path}")


if __name__ == "__main__":
    main()
