"""Check the data files in data/ (companies, claims, rounds, fx, sectors) against docs/data-model.md.

Usage: python scripts/check_data.py
Exits with status 1 and prints readable errors if anything is wrong.
"""
import csv
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data"
COMPANIES_CSV = DATA / "companies.csv"
CLAIMS_CSV = DATA / "claims.csv"

ROOT = DATA.parent
COMPANY_COLUMNS = [
    "name", "website", "fund", "is_highlight", "is_exit", "logo", "logo_background", "logo_origin", "logo_source", "researched_on", "logo_crop",
]
CLAIM_COLUMNS = ["company", "field", "value", "source_url", "basis", "confidence", "note"]
SECTOR_COLUMNS = ["sub_sector", "sector"]
FX_COLUMNS = ["currency", "year", "rate", "source_url"]
ROUND_COLUMNS = [
    "company", "year", "type", "reported_amount", "reported_currency", "size_usd", "co_investors",
    "norte_participated", "source_url", "basis", "confidence", "note",
]
# In funding order. Extensions and bridges take their base type; debt and credit facilities are "debt".
ROUND_TYPES = [
    "angel", "pre_seed", "seed", "series_a", "series_b", "series_c", "series_d", "series_e",
    "series_f_plus", "unknown", "debt",
]
AMOUNT_COLUMNS = ["reported_amount", "reported_currency", "size_usd"]
CURRENCY = re.compile(r"[A-Z]{3}")

# The claim fields from docs/data-model.md. A single-value field has at most one row per company
# (conflicting sources are weighed and the discarded values go in the note); a list field has one
# row per value.
SINGLE_VALUE_FIELDS = [
    "description",
    "long_description",
    "investment_thesis",
    "sub_sector",
    "hq",
    "hq_at_first_investment",
    "year_founded",
    "status",
    "business_model",
    "acquirer",
    "acquisition_year",
]
LIST_FIELDS = ["founder", "market", "accelerator", "milestone"]
ALLOWED_FIELDS = SINGLE_VALUE_FIELDS + LIST_FIELDS
ALLOWED_STATUS = ["stealth", "active", "inactive", "closed"]
ALLOWED_BUSINESS_MODELS = ["b2b", "b2c", "b2b2c"]
FIRST_YEAR = 1990
CITY_COUNTRY = re.compile(r"[^,]+, [^,]+")
MILESTONE = re.compile(r"(\d{4})(?:-(0[1-9]|1[0-2])(?:-(\d{2}))?)?: \S")
ALLOWED_BASIS = ["reported", "estimated"]
ALLOWED_CONFIDENCE = ["high", "medium", "low"]
ALLOWED_FUNDS = ["I", "II"]
ALLOWED_FLAGS = ["TRUE", "FALSE"]
ALLOWED_NORTE = ["TRUE", "FALSE", "UNKNOWN"]
ALLOWED_LOGO_ORIGINS = ["company-site", "web-search", "manual"]
# The circle's fill is a "#rrggbb" color (set by the logo studio, ADR 0015). The old words (which page
# background the logo is legible on) stay valid until every logo is confirmed; empty means not reviewed yet.
ALLOWED_LOGO_BACKGROUNDS = ["dark", "light", "both"]
LOGO_COLOR = re.compile(r"#[0-9a-fA-F]{6}")
# Documented exception (ADR 0004): no Original logo was found anywhere public, so these companies
# keep the recolored logo from the Firm's portfolio page. Add a name here only with an ADR note.
NORTE_LOGO_EXCEPTIONS = {"glue"}


def is_valid_url(url):
    if any(c.isspace() for c in url):
        return False
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and "." in parsed.netloc


def _read(path, expected_columns):
    """Return (rows, errors). Each row is a dict plus a '_line' number."""
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != expected_columns:
            return [], [
                f"{path.name}: columns must be exactly {', '.join(expected_columns)} "
                f"(found: {', '.join(reader.fieldnames or [])})"
            ]
        rows = []
        for row in reader:
            # A quoted value can span lines; report the line the row starts on.
            extra_lines = sum((v or "").count("\n") for v in row.values() if isinstance(v, str))
            row = {k: (v or "").strip() for k, v in row.items() if k is not None}
            row["_line"] = reader.line_num - extra_lines
            rows.append(row)
    return rows, []


def _is_crop(text):
    """x,y,w,h as fractions of the source image: a box with area, at most 3x the image, that overlaps it.

    It may extend past the image's edges: that is the padding added around an oversized logo."""
    parts = text.split(",")
    try:
        x, y, w, h = (float(p) for p in parts)
    except ValueError:
        return False
    return len(parts) == 4 and 0 < w <= 3 and 0 < h <= 3 and x < 1 and y < 1 and x + w > 0 and y + h > 0


def _check_logo(row, where, root):
    """An empty logo is valid (manual follow-up); a set logo needs a recorded origin and source."""
    logo, origin, source = row["logo"], row["logo_origin"], row["logo_source"]
    if not logo:
        if origin or source or row["logo_background"] or row["logo_crop"]:
            return [f"{where}: logo is empty but logo_origin/logo_source/logo_background/logo_crop are set (clear them)"]
        return []
    errors = []
    background = row["logo_background"]
    if background and background not in ALLOWED_LOGO_BACKGROUNDS and not LOGO_COLOR.fullmatch(background):
        errors.append(
            f"{where}: logo_background '{background}' must be #rrggbb, one of {', '.join(ALLOWED_LOGO_BACKGROUNDS)}, or empty"
        )
    if row["logo_crop"] and not _is_crop(row["logo_crop"]):
        errors.append(f"{where}: logo_crop '{row['logo_crop']}' must be four fractions as x,y,w,h (a box of at most 3x the image that overlaps it)")
    if not (Path(root) / logo).is_file():
        errors.append(f"{where}: logo file '{logo}' does not exist")
    if origin not in ALLOWED_LOGO_ORIGINS:
        errors.append(
            f"{where}: logo_origin '{origin}' must be one of {', '.join(ALLOWED_LOGO_ORIGINS)}"
        )
    if not is_valid_url(source):
        errors.append(f"{where}: logo_source '{source}' is not a valid URL")
    elif _is_norte_domain(source) and row["name"].casefold() not in NORTE_LOGO_EXCEPTIONS:
        errors.append(f"{where}: logo_source '{source}' is on norte.ventures (Norte logos are not Original logos)")
    return errors


def _is_norte_domain(url):
    host = (urlparse(url).hostname or "").lower()
    return host == "norte.ventures" or host.endswith(".norte.ventures")


def follow_up_companies(rows):
    """Names of companies with no logo, for the manual-follow-up list."""
    return [r["name"] for r in rows if not r["logo"]]


def check_companies(rows, filename="companies.csv", root=ROOT):
    errors = []
    seen = {}
    for row in rows:
        where = f"{filename} line {row['_line']}"
        name = row["name"]
        if not name:
            errors.append(f"{where}: name is empty")
        else:
            key = name.casefold()
            if key in seen:
                errors.append(f"{where}: duplicate of line {seen[key]} ('{name}')")
            else:
                seen[key] = row["_line"]
        if not is_valid_url(row["website"]):
            errors.append(f"{where}: website '{row['website']}' is not a valid URL")
        if row["fund"] not in ALLOWED_FUNDS:
            errors.append(f"{where}: fund '{row['fund']}' must be one of {', '.join(ALLOWED_FUNDS)}")
        errors += _check_logo(row, where, root)
        for flag in ("is_highlight", "is_exit"):
            if row[flag] not in ALLOWED_FLAGS:
                errors.append(f"{where}: {flag} '{row[flag]}' must be TRUE or FALSE")
        errors += _check_researched_on(row["researched_on"], where)
    return errors


def _check_researched_on(value, where):
    """Empty means not researched yet; otherwise an ISO date (YYYY-MM-DD) that is not in the future."""
    if not value:
        return []
    try:
        day = date.fromisoformat(value)
    except ValueError:
        day = None
    if day is None or len(value) != 10:
        return [f"{where}: researched_on '{value}' must be a date like 2026-11-18"]
    if day > date.today():
        return [f"{where}: researched_on '{value}' is in the future"]
    return []


def _has_line_break(value):
    return "\n" in value or "\r" in value


def is_year(value):
    return value.isdigit() and len(value) == 4 and FIRST_YEAR <= int(value) <= date.today().year


def _check_year(value, label):
    if is_year(value):
        return []
    return [f"{label} '{value}' must be a year from {FIRST_YEAR} to {date.today().year}"]


def _is_milestone(value):
    match = MILESTONE.match(value)
    if not match or not is_year(match.group(1)):
        return False
    year, month, day = match.groups()
    if day:
        try:
            date(int(year), int(month), int(day))
        except ValueError:
            return False
    return True


def _check_claim_value(field, value):
    """Format rules for fields whose values are not free text."""
    if field in ("year_founded", "acquisition_year"):
        return _check_year(value, field)
    if field == "status" and value not in ALLOWED_STATUS:
        return [f"status '{value}' must be one of {', '.join(ALLOWED_STATUS)}"]
    if field == "business_model" and value not in ALLOWED_BUSINESS_MODELS:
        return [f"business_model '{value}' must be one of {', '.join(ALLOWED_BUSINESS_MODELS)}"]
    if field in ("hq", "hq_at_first_investment") and not CITY_COUNTRY.fullmatch(value):
        return [f"{field} '{value}' must look like 'City, Country'"]
    if field == "milestone" and not _is_milestone(value):
        return [f"milestone '{value}' must start with a date and a colon, like '2021: ...' or '2021-03: ...'"]
    return []


def _years_founded(claims):
    """Each company's valid year_founded, keyed by casefolded company name."""
    return {r["company"].casefold(): r["value"] for r in claims if r["field"] == "year_founded" and is_year(r["value"])}


def _check_claim_dates(rows, filename):
    """An acquisition cannot come before the company was founded."""
    founded = _years_founded(rows)
    errors = []
    for row in rows:
        start = founded.get(row["company"].casefold())
        if row["field"] == "acquisition_year" and start and is_year(row["value"]) and row["value"] < start:
            errors.append(
                f"{filename} line {row['_line']}: acquisition_year {row['value']} is before year_founded {start}"
            )
    return errors


def _check_sourcing(row, where, kind):
    """Rules shared by claims and rounds: a valid source link, a Basis (with a note if estimated), a Confidence."""
    errors = []
    if not row["source_url"]:
        errors.append(f"{where}: source_url is empty (every {kind} needs a source link)")
    elif not is_valid_url(row["source_url"]):
        errors.append(f"{where}: source_url '{row['source_url']}' is not a valid URL")
    if row["basis"] not in ALLOWED_BASIS:
        errors.append(f"{where}: basis '{row['basis']}' must be one of {', '.join(ALLOWED_BASIS)}")
    elif row["basis"] == "estimated" and not row["note"]:
        errors.append(f"{where}: estimated {kind} needs a note explaining the reasoning")
    if row["confidence"] not in ALLOWED_CONFIDENCE:
        errors.append(f"{where}: confidence '{row['confidence']}' must be one of {', '.join(ALLOWED_CONFIDENCE)}")
    return errors


def check_claims(rows, company_names, filename="claims.csv", sub_sectors=()):
    known = {n.casefold() for n in company_names}
    listed_sub_sectors = {s.casefold() for s in sub_sectors}
    errors = []
    seen = {}
    single = {}
    for row in rows:
        where = f"{filename} line {row['_line']}"
        if row["company"].casefold() not in known:
            errors.append(f"{where}: unknown company '{row['company']}' (not in companies.csv)")
        if row["field"] not in ALLOWED_FIELDS:
            errors.append(
                f"{where}: field '{row['field']}' is not allowed (use one of {', '.join(ALLOWED_FIELDS)})"
            )
        if not row["value"]:
            errors.append(f"{where}: value is empty")
        elif _has_line_break(row["value"]):
            errors.append(f"{where}: value has a line break (keep each value on one line; split long text into rows)")
        else:
            errors += [f"{where}: {e}" for e in _check_claim_value(row["field"], row["value"])]
            if row["field"] == "sub_sector" and row["value"].casefold() not in listed_sub_sectors:
                errors.append(f"{where}: sub_sector '{row['value']}' is not in sectors.csv (add it there first)")
        errors += _check_sourcing(row, where, "claim")
        if row["field"] in SINGLE_VALUE_FIELDS:
            key = (row["company"].casefold(), row["field"])
            if key in single:
                errors.append(
                    f"{where}: second '{row['field']}' for {row['company']} (first on line {single[key]}); "
                    "keep one value: weigh the sources, keep the most likely one and put the discarded values in its note"
                )
                continue
            single[key] = row["_line"]
        key = (row["company"].casefold(), row["field"], row["value"].casefold())
        if key in seen:
            errors.append(f"{where}: duplicate of line {seen[key]} (same company, field and value)")
        else:
            seen[key] = row["_line"]
    return errors + _check_claim_dates(rows, filename)


def check_sectors(rows, filename="sectors.csv"):
    """Each sub-sector appears once and has a sector."""
    errors = []
    seen = {}
    for row in rows:
        where = f"{filename} line {row['_line']}"
        if not row["sub_sector"]:
            errors.append(f"{where}: sub_sector is empty")
            continue
        if not row["sector"]:
            errors.append(f"{where}: sector is empty ('{row['sub_sector']}')")
        key = row["sub_sector"].casefold()
        if key in seen:
            errors.append(f"{where}: duplicate of line {seen[key]} ('{row['sub_sector']}')")
        else:
            seen[key] = row["_line"]
    return errors


def _parse_rate(value):
    """A positive decimal written with a dot, or None."""
    try:
        rate = float(value)
    except ValueError:
        return None
    return rate if rate > 0 and re.fullmatch(r"\d+(\.\d+)?", value) else None


def check_fx(rows, filename="fx.csv"):
    """One annual average rate per currency and year, in units of that currency per US dollar."""
    errors = []
    seen = {}
    for row in rows:
        where = f"{filename} line {row['_line']}"
        currency = row["currency"]
        if not CURRENCY.fullmatch(currency) or currency == "USD":
            errors.append(f"{where}: currency '{currency}' must be a three-letter code like BRL (not USD)")
        errors += [f"{where}: {e}" for e in _check_year(row["year"], "year")]
        if _parse_rate(row["rate"]) is None:
            errors.append(f"{where}: rate '{row['rate']}' must be a positive number like 5.3956")
        if not is_valid_url(row["source_url"]):
            errors.append(f"{where}: source_url '{row['source_url']}' is not a valid URL")
        key = (currency, row["year"])
        if key in seen:
            errors.append(f"{where}: duplicate of line {seen[key]} (one rate per currency and year)")
        else:
            seen[key] = row["_line"]
    return errors


def _is_whole_number(value):
    return value.isdigit() and int(value) > 0


def _check_amount(row, rates):
    """The reported amount and currency, and the USD size computed from them with fx.csv.

    All three empty: size not disclosed. size_usd alone may stay empty while the year's rate is unpublished."""
    amount, currency, size = (row[c] for c in AMOUNT_COLUMNS)
    if not (amount or currency or size):
        return []
    if not (amount and currency):
        if amount or currency:
            return ["fill reported_amount and reported_currency together, or leave all three amount columns empty"]
        return ["size_usd needs reported_amount and reported_currency (the figure as the Source reports it)"]
    errors = [f"{c} '{row[c]}' must be a whole number" for c in ("reported_amount", "size_usd")
              if row[c] and not _is_whole_number(row[c])]
    if not CURRENCY.fullmatch(currency):
        errors.append(f"reported_currency '{currency}' must be a three-letter code like BRL or USD")
    if errors or not is_year(row["year"]):
        return errors  # a bad year is reported on its own
    if currency == "USD":
        expected, how = int(amount), f"{amount} USD"
    else:
        rate = rates.get((currency, row["year"]))
        if rate is None:
            if not size:
                return []  # waiting for the annual average to be published
            return [f"no {currency} rate for {row['year']} in fx.csv (add the annual average there first)"]
        expected, how = round(int(amount) / rate), f"{amount} {currency} at {rate:g}"
    if not size:
        return [f"size_usd is empty: compute size_usd from the {row['year']} {currency} rate in fx.csv (expected {expected})"
                if currency != "USD" else f"size_usd is empty (expected {expected})"]
    if int(size) != expected:
        return [f"size_usd {size} does not match {how} (expected {expected})"]
    return []


def check_rounds(rows, company_names, filename="rounds.csv", fx_rows=()):
    known = {n.casefold() for n in company_names}
    rates = {(r["currency"], r["year"]): _parse_rate(r["rate"]) for r in fx_rows if _parse_rate(r["rate"])}
    errors = []
    seen = {}
    for row in rows:
        where = f"{filename} line {row['_line']}"
        if row["company"].casefold() not in known:
            errors.append(f"{where}: unknown company '{row['company']}' (not in companies.csv)")
        errors += [f"{where}: {e}" for e in _check_year(row["year"], "year")]
        if row["type"] not in ROUND_TYPES:
            errors.append(f"{where}: type '{row['type']}' must be one of {', '.join(ROUND_TYPES)}")
        errors += [f"{where}: {e}" for e in _check_amount(row, rates)]
        if _has_line_break(row["co_investors"]):
            errors.append(f"{where}: co_investors has a line break (separate names with '; ')")
        if row["norte_participated"] not in ALLOWED_NORTE:
            errors.append(f"{where}: norte_participated '{row['norte_participated']}' must be TRUE, FALSE or UNKNOWN")
        errors += _check_sourcing(row, where, "round")
        # One row per Round. A company can take several debt facilities, or Rounds of unknown type, in
        # one year, so those are told apart by amount.
        key = (row["company"].casefold(), row["year"], row["type"])
        if row["type"] in ("debt", "unknown"):
            key += (row["reported_amount"],)
        if key in seen:
            errors.append(
                f"{where}: second {row['type']} in {row['year']} for {row['company']} (duplicate of line {seen[key]}); "
                "keep one row: weigh the sources, keep the most likely figure and put the discarded ones in its note"
            )
        else:
            seen[key] = row["_line"]
    return errors


def _check_rounds_after_founding(rounds, claims, filename="rounds.csv"):
    founded = _years_founded(claims)
    errors = []
    for row in rounds:
        start = founded.get(row["company"].casefold())
        if start and is_year(row["year"]) and row["year"] < start:
            errors.append(f"{filename} line {row['_line']}: round year {row['year']} is before year_founded {start}")
    return errors


def _read_optional(path, columns):
    """Like _read, but a file that does not exist yet is an empty table."""
    return _read(path, columns) if path.exists() else ([], [])


def check_files(data=DATA, root=ROOT):
    """Check every data file in the `data` folder; return error messages (empty means everything passes)."""
    data = Path(data)
    companies, errors = _read(data / "companies.csv", COMPANY_COLUMNS)
    errors += check_companies(companies, "companies.csv", root)
    names = [c["name"] for c in companies]

    sectors, read_errors = _read_optional(data / "sectors.csv", SECTOR_COLUMNS)
    errors += read_errors + check_sectors(sectors)

    fx, read_errors = _read_optional(data / "fx.csv", FX_COLUMNS)
    errors += read_errors + check_fx(fx)

    claims, read_errors = _read_optional(data / "claims.csv", CLAIM_COLUMNS)
    errors += read_errors + check_claims(claims, names, sub_sectors=[r["sub_sector"] for r in sectors])

    rounds, read_errors = _read_optional(data / "rounds.csv", ROUND_COLUMNS)
    errors += read_errors + check_rounds(rounds, names, fx_rows=fx) + _check_rounds_after_founding(rounds, claims)
    return errors


def main():
    errors = check_files()
    if errors:
        print(f"{len(errors)} problem(s) found:")
        for e in errors:
            print(f"  - {e}")
        raise SystemExit(1)
    companies, _ = _read(COMPANIES_CSV, COMPANY_COLUMNS)
    missing = follow_up_companies(companies)
    if missing:
        print(f"{len(missing)} company(ies) without a logo (manual follow-up): {', '.join(missing)}")
    note = "" if CLAIMS_CSV.exists() else " (no claims.csv yet, so no claims were checked)"
    print(f"All checks passed{note}.")


if __name__ == "__main__":
    main()
