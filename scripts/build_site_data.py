"""Build the site's one data file (site/src/data/companies.json) from data/.

Usage: python scripts/build_site_data.py
Runs the data check first and refuses to write anything if it fails.
One entry per Portfolio company: slug, name, Fund, website, logo path, `fields` (single-value facts as
{value, basis, confidence, source}; a field research found nothing for is absent), `lists` (founders, markets,
accelerators, milestones, each a list of such fields), `rounds` (each with its own provenance, USD size and
Norte's participation: true, false or null for unknown), `first_investment` and `follow_on`. Notes are not shipped.
"""
import json
import re
import unicodedata
from pathlib import Path

from check_data import CLAIM_COLUMNS, COMPANY_COLUMNS, DATA, ROOT, ROUND_COLUMNS, SECTOR_COLUMNS, _read, _read_optional, check_files
from derive import first_investment, follow_on, in_order
from logo_circle import circle_path, has_circle_choice

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


# Every single-value claim field except sub_sector (shipped only through its Sector), and the list fields.
# Notes are never shipped.
SINGLE_FIELDS = [
    "description", "long_description", "investment_thesis", "sub_sector", "hq", "hq_at_first_investment",
    "year_founded", "status", "business_model", "acquirer", "acquisition_year",
]
INTEGER_FIELDS = {"year_founded", "acquisition_year"}
LIST_FIELDS = {"founder": "founders", "market": "markets", "accelerator": "accelerators", "milestone": "milestones"}


def _field(claim, value):
    return {"value": value, "basis": claim["basis"], "confidence": claim["confidence"], "source": claim["source_url"]}


def _fields(claims, sector_of):
    """A company's single-value fields from its Claims. Sector is the mapped Sector of its sub_sector Claim."""
    by_field = {c["field"]: c for c in claims}
    fields = {}
    for name in SINGLE_FIELDS:
        if name in by_field:
            claim = by_field[name]
            fields[name] = _field(claim, int(claim["value"]) if name in INTEGER_FIELDS else claim["value"])
    sub_sector = by_field.get("sub_sector")
    if sub_sector and sector_of.get(sub_sector["value"].casefold()):
        fields["sector"] = _field(sub_sector, sector_of[sub_sector["value"].casefold()])
    return fields


def _lists(claims):
    """A company's list fields, one {value, basis, confidence, source} per row, in file order.
    Milestones split `date: event` into `date` and `value`, and come earliest first."""
    lists = {key: [] for key in LIST_FIELDS.values()}
    for claim in claims:
        key = LIST_FIELDS.get(claim["field"])
        if key == "milestones":
            date, event = claim["value"].split(": ", 1)
            lists[key].append({**_field(claim, event), "date": date})
        elif key:
            lists[key].append(_field(claim, claim["value"]))
    lists["milestones"].sort(key=lambda m: m["date"])
    return lists


NORTE = {"TRUE": True, "FALSE": False, "UNKNOWN": None}


def _round(row):
    return {
        "year": int(row["year"]),
        "type": row["type"],
        "size_usd": int(row["size_usd"]) if row["size_usd"] else None,
        "norte": NORTE[row["norte_participated"]],
        "co_investors": [i for i in row["co_investors"].split("; ") if i],
        "basis": row["basis"],
        "confidence": row["confidence"],
        "source": row["source_url"],
    }


def build(data=DATA, root=ROOT):
    """Return the site data; exit with the check's errors if the data is not valid."""
    errors = check_files(data, root)
    if errors:
        raise SystemExit("Data check failed, nothing built:\n" + "\n".join(f"  - {e}" for e in errors))
    rows, _ = _read(Path(data) / "companies.csv", COMPANY_COLUMNS)
    claims, _ = _read(Path(data) / "claims.csv", CLAIM_COLUMNS)
    round_rows, _ = _read_optional(Path(data) / "rounds.csv", ROUND_COLUMNS)
    sectors, _ = _read(Path(data) / "sectors.csv", SECTOR_COLUMNS)
    sector_of = {r["sub_sector"].casefold(): r["sector"] for r in sectors}
    slugs = _unique_slugs([r["name"] for r in rows])
    return {
        "companies": [
            _company(slug, r, claims, round_rows, sector_of, root)
            for slug, r in zip(slugs, rows)
        ]
    }


def _logo(row, root):
    """The logo circle when one has been built, otherwise the raw logo; relative to the site folder."""
    if has_circle_choice(row) and (Path(root) / circle_path(row["logo"])).is_file():
        return circle_path(row["logo"]).as_posix().removeprefix("site/")
    return row["logo"].removeprefix("site/")


def _company(slug, r, claims, round_rows, sector_of, root):
    mine = [c for c in claims if c["company"] == r["name"]]
    own_rounds = in_order(x for x in round_rows if x["company"] == r["name"])
    first = first_investment(own_rounds)
    return {
        "slug": slug,
        "name": r["name"],
        "fund": r["fund"],
        "website": r["website"],
        # The site is served from its own folder, so the repo's "site/" prefix is dropped.
        "logo": _logo(r, root),
        "fields": _fields(mine, sector_of),
        "lists": _lists(mine),
        "rounds": [_round(x) for x in own_rounds],
        "first_investment": _round(first) if first else None,
        "follow_on": follow_on(own_rounds),
    }


def main():
    data = build()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Wrote {len(data['companies'])} companies to {OUTPUT}")


if __name__ == "__main__":
    main()
