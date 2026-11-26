"""Build the site's one data file (site/src/data/companies.json) from data/.

Usage: python scripts/build_site_data.py
Runs the data check first and refuses to write anything if it fails.
First version: one entry per Portfolio company with slug, name, Fund and logo path.
"""
import json
import re
import unicodedata
from pathlib import Path

from check_data import COMPANIES_CSV, COMPANY_COLUMNS, DATA, ROOT, _read, check_files

OUTPUT = ROOT / "site" / "src" / "data" / "companies.json"


def slugify(name):
    """Lowercase ASCII words joined by hyphens: the company's stable address."""
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_name.lower()).strip("-")


def _unique_slugs(names):
    seen, slugs = {}, []
    for name in names:
        base = slugify(name)
        seen[base] = seen.get(base, 0) + 1
        slugs.append(base if seen[base] == 1 else f"{base}-{seen[base]}")
    return slugs


def build(data=DATA, root=ROOT):
    """Return the site data; exit with the check's errors if the data is not valid."""
    errors = check_files(data, root)
    if errors:
        raise SystemExit("Data check failed, nothing built:\n" + "\n".join(f"  - {e}" for e in errors))
    rows, _ = _read(Path(data) / "companies.csv", COMPANY_COLUMNS)
    slugs = _unique_slugs([r["name"] for r in rows])
    return {
        "companies": [
            {
                "slug": slug,
                "name": r["name"],
                "fund": r["fund"],
                # The site is served from its own folder, so the repo's "site/" prefix is dropped.
                "logo": r["logo"].removeprefix("site/"),
            }
            for slug, r in zip(slugs, rows)
        ]
    }


def main():
    data = build()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Wrote {len(data['companies'])} companies to {OUTPUT}")


if __name__ == "__main__":
    main()
