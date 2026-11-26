"""Build the site's one data file (site/src/data/companies.json) from data/.

Usage: python scripts/build_site_data.py
Runs the data check first and refuses to write anything if it fails.
One entry per Portfolio company: slug, name, Fund, logo path and `fields`, the card's facts as
{value, basis, confidence, source}. A field research found nothing for is absent.
"""
import json
import re
import unicodedata
from pathlib import Path

from check_data import CLAIM_COLUMNS, COMPANY_COLUMNS, DATA, ROOT, SECTOR_COLUMNS, _read, check_files

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


# Claim fields the Company card shows; the profile ticket adds more.
CARD_FIELDS = ["description", "year_founded"]
INTEGER_FIELDS = {"year_founded"}


def _field(claim, value):
    return {"value": value, "basis": claim["basis"], "confidence": claim["confidence"], "source": claim["source_url"]}


def _card_fields(claims, sector_of):
    """The card's fields from one company's Claims. Sector is the mapped Sector of its sub_sector Claim."""
    by_field = {c["field"]: c for c in claims}
    fields = {}
    for name in CARD_FIELDS:
        if name in by_field:
            claim = by_field[name]
            fields[name] = _field(claim, int(claim["value"]) if name in INTEGER_FIELDS else claim["value"])
    sub_sector = by_field.get("sub_sector")
    if sub_sector and sector_of.get(sub_sector["value"].casefold()):
        fields["sector"] = _field(sub_sector, sector_of[sub_sector["value"].casefold()])
    return fields


def build(data=DATA, root=ROOT):
    """Return the site data; exit with the check's errors if the data is not valid."""
    errors = check_files(data, root)
    if errors:
        raise SystemExit("Data check failed, nothing built:\n" + "\n".join(f"  - {e}" for e in errors))
    rows, _ = _read(Path(data) / "companies.csv", COMPANY_COLUMNS)
    claims, _ = _read(Path(data) / "claims.csv", CLAIM_COLUMNS)
    sectors, _ = _read(Path(data) / "sectors.csv", SECTOR_COLUMNS)
    sector_of = {r["sub_sector"].casefold(): r["sector"] for r in sectors}
    slugs = _unique_slugs([r["name"] for r in rows])
    return {
        "companies": [
            {
                "slug": slug,
                "name": r["name"],
                "fund": r["fund"],
                # The site is served from its own folder, so the repo's "site/" prefix is dropped.
                "logo": r["logo"].removeprefix("site/"),
                "fields": _card_fields([c for c in claims if c["company"] == r["name"]], sector_of),
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
