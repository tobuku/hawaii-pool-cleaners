"""Batch-add BreadcrumbList schema to all area pages."""
import os, re, glob

area_dirs = sorted(glob.glob("areas/*/index.html"))
updated = 0
skipped = 0

for fpath in area_dirs:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if "BreadcrumbList" in content:
        skipped += 1
        continue

    # Extract area name from title
    title_match = re.search(r"<title>.*?in\s+(.+?),\s*(?:Oahu|Hawaii|East)", content)
    if not title_match:
        title_match = re.search(r"<title>.*?in\s+(.+?)\s*[|,]", content)
    if not title_match:
        # Fallback: derive from directory name
        slug = os.path.basename(os.path.dirname(fpath))
        area_name = slug.replace("-", " ").title()
    else:
        area_name = title_match.group(1).strip()

    # Find insertion point: after existing JSON-LD </script>, before <link rel="icon">
    old = '</script>\n<link rel="icon" href="/wp-content/uploads/2024/06/cropped-Hawaii-Pool-Cleaners-Logo-192x192.jpg" sizes="192x192">'

    if old not in content:
        print(f"SKIP (no insert point): {fpath} - {area_name}")
        skipped += 1
        continue

    breadcrumb_json = (
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Home","item":"https://hawaiipoolcleaners.com/"},'
        '{"@type":"ListItem","position":2,"name":"Service Areas","item":"https://hawaiipoolcleaners.com/areas/"},'
        '{"@type":"ListItem","position":3,"name":"' + area_name + '"}'
        "]}"
    )

    new = (
        "</script>\n"
        '<script type="application/ld+json">\n'
        + breadcrumb_json
        + "\n</script>\n"
        '<link rel="icon" href="/wp-content/uploads/2024/06/cropped-Hawaii-Pool-Cleaners-Logo-192x192.jpg" sizes="192x192">'
    )

    content = content.replace(old, new, 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    updated += 1
    print(f"OK: {area_name}")

print(f"\nDone: {updated} updated, {skipped} skipped")
