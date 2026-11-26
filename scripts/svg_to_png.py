"""Convert every SVG logo in data/companies.csv to a transparent PNG (about 1024px on the long side).

SVGs have no reliable pixel size in the browser, which breaks the logo studio's crop, so logos are kept as
PNGs. Updates the `logo` column, deletes the SVG and any stale circle; logo_source, crop and fill are kept.
Needs Pillow and PyMuPDF. Safe to rerun (run it again after `scripts/fetch_logos.py` brings in new SVGs).
"""
import csv
from pathlib import Path

from logo_circle import COMPANIES_CSV, ROOT, circle_path, open_logo


def convert_rows(rows, root=ROOT):
    """Convert each row's SVG logo in place; returns (converted names, failures)."""
    converted, failed = [], []
    for row in rows:
        if not row["logo"].lower().endswith(".svg"):
            continue
        svg = root / row["logo"]
        png = svg.with_suffix(".png")
        try:
            open_logo(svg).convert("RGBA").save(png, "PNG")
        except Exception as error:  # one bad SVG must not stop the rest
            failed.append(f"{row['name']} ({error})")
            continue
        (root / circle_path(row["logo"])).unlink(missing_ok=True)  # same stem: rebuilt from the PNG by the studio
        svg.unlink()
        row["logo"] = str(Path(row["logo"]).with_suffix(".png")).replace("\\", "/")
        converted.append(row["name"])
    return converted, failed


def main():
    with COMPANIES_CSV.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        columns, rows = reader.fieldnames, list(reader)
    converted, failed = convert_rows(rows)
    with COMPANIES_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Converted {len(converted)} SVG logo(s) to PNG.")
    if failed:
        print(f"Failed {len(failed)}: {'; '.join(failed)}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
