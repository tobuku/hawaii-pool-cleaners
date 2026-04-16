#!/usr/bin/env python3
"""
deploy_areas.py
Pushes the next batch of 5-7 area pages to GitHub Pages (one batch per day).
Run once per day: python deploy_areas.py

State is tracked in areas_deploy_state.json
Pages must already exist in areas/ (run generate_area_pages.py first).
"""

import os
import sys
import json
import subprocess
from datetime import date

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "areas_deploy_state.json")
BATCH_SIZE = 6  # change to 5 or 7 if preferred

# Full ordered list of area slugs — edit order here to change release sequence
SLUGS = [
    "honolulu",
    "kailua",
    "kaneohe",
    "kapolei",
    "mililani",
    "pearl-city",
    "hawaii-kai",
    "aiea",
    "waipahu",
    "ewa-beach",
    "ewa-gentry",
    "waikiki",
    "kaimuki",
    "manoa",
    "salt-lake",
    "aliamanu",
    "moanalua",
    "pearl-harbor",
    "downtown-honolulu",
    "kakaako",
    "ala-moana",
    "kapahulu",
    "mccully",
    "kalihi",
    "punchbowl",
    "palolo",
    "aina-haina",
    "niu-valley",
    "kalama-valley",
    "kahala",
    "enchanted-lake",
    "lanikai",
    "waimanalo",
    "kaneohe-bay",
    "ahuimanu",
    "makakilo",
    "iroquois-point",
    "hickam-housing",
    "schofield-barracks",
    "wheeler-army-airfield",
    "tripler-army-medical-center",
    "haleiwa",
    "waialua",
    "kahuku",
    "laie",
    "hauula",
    "kaaawa",
    "waianae",
    "nanakuli",
    "maili",
    "makaha",
    "whitmore-village",
    "campbell-industrial-park",
]


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"pushed": [], "batches": []}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip())
    return result.returncode


def main():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    state = load_state()
    pushed = set(state.get("pushed", []))

    remaining = [s for s in SLUGS if s not in pushed]

    if not remaining:
        print("All 53 area pages have been pushed. Nothing left to deploy.")
        return

    batch = remaining[:BATCH_SIZE]
    today = str(date.today())

    # Verify files exist
    missing = []
    for slug in batch:
        path = os.path.join(repo_dir, "areas", slug, "index.html")
        if not os.path.exists(path):
            missing.append(slug)
    if missing:
        print(f"ERROR: Missing generated files for: {', '.join(missing)}")
        print("Run generate_area_pages.py first.")
        sys.exit(1)

    print(f"\nBatch for {today} — {len(batch)} pages:")
    for s in batch:
        print(f"  areas/{s}/index.html")

    print("\nStaging files...")
    for slug in batch:
        rc = run(f'git add "areas/{slug}/index.html"', cwd=repo_dir)
        if rc != 0:
            print(f"ERROR: git add failed for {slug}")
            sys.exit(1)

    # Also stage state file
    save_state({"pushed": list(pushed | set(batch)), "batches": state.get("batches", []) + [{"date": today, "slugs": batch}]})
    run(f'git add areas_deploy_state.json', cwd=repo_dir)

    names = ", ".join(s.replace("-", " ").title() for s in batch)
    commit_msg = f"Add area pages: {names}"

    print(f"\nCommitting: {commit_msg}")
    rc = run(f'git commit -m "{commit_msg}"', cwd=repo_dir)
    if rc != 0:
        print("ERROR: git commit failed")
        sys.exit(1)

    print("\nPushing to GitHub Pages...")
    rc = run("git push origin main", cwd=repo_dir)
    if rc != 0:
        print("ERROR: git push failed")
        sys.exit(1)

    remaining_after = [s for s in SLUGS if s not in (pushed | set(batch))]
    days_left = -(-len(remaining_after) // BATCH_SIZE)  # ceiling division

    print(f"\nDone. {len(batch)} pages pushed.")
    print(f"Pushed so far: {len(pushed) + len(batch)}/{len(SLUGS)}")
    print(f"Remaining: {len(remaining_after)} pages (~{days_left} more days at {BATCH_SIZE}/day)")
    if remaining_after:
        print(f"Next batch: {', '.join(remaining_after[:BATCH_SIZE])}")
    else:
        print("All pages are now live!")


if __name__ == "__main__":
    main()
