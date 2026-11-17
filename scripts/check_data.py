"""Check the data files in data/ for completeness and data types.

Usage: python scripts/check_data.py
Exits with status 1 and prints readable errors if anything is wrong.
"""
import csv
import sys
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data"
COMPANIES_CSV = DATA / "companies.csv"
CLAIMS_CSV = DATA / "claims.csv"

COMPANY_COLUMNS = ["name", "website", "fund", "is_highlight", "is_exit"]
CLAIM_COLUMNS = ["company", "field", "value", "source_url", "basis", "confidence", "note"]

# The Batch 1 fields from docs/stages.md (stage 2, Pilot).
ALLOWED_FIELDS = [
    "description",
    "sector",
    "location",
    "year_founded",
    "investment_year",
    "status",
    "round_size",
    "co_investors",
    "founder_names",
]
ALLOWED_BASIS = ["reported", "estimated"]
ALLOWED_CONFIDENCE = ["high", "medium", "low"]
ALLOWED_FUNDS = ["I", "II"]
ALLOWED_FLAGS = ["TRUE", "FALSE"]


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
            row = {k: (v or "").strip() for k, v in row.items() if k is not None}
            row["_line"] = reader.line_num
            rows.append(row)
    return rows, []


def check_companies(rows, filename="companies.csv"):
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
        for flag in ("is_highlight", "is_exit"):
            if row[flag] not in ALLOWED_FLAGS:
                errors.append(f"{where}: {flag} '{row[flag]}' must be TRUE or FALSE")
    return errors


def check_claims(rows, company_names, filename="claims.csv"):
    known = {n.casefold() for n in company_names}
    errors = []
    seen = {}
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
        if not row["source_url"]:
            errors.append(f"{where}: source_url is empty (every claim needs a source link)")
        elif not is_valid_url(row["source_url"]):
            errors.append(f"{where}: source_url '{row['source_url']}' is not a valid URL")
        if row["basis"] not in ALLOWED_BASIS:
            errors.append(f"{where}: basis '{row['basis']}' must be one of {', '.join(ALLOWED_BASIS)}")
        elif row["basis"] == "estimated" and not row["note"]:
            errors.append(f"{where}: estimated claim needs a note explaining the reasoning")
        if row["confidence"] not in ALLOWED_CONFIDENCE:
            errors.append(
                f"{where}: confidence '{row['confidence']}' must be one of {', '.join(ALLOWED_CONFIDENCE)}"
            )
        key = (row["company"].casefold(), row["field"], row["value"].casefold())
        if key in seen:
            errors.append(f"{where}: duplicate of line {seen[key]} (same company, field and value)")
        else:
            seen[key] = row["_line"]
    return errors


def check_files(companies_path=COMPANIES_CSV, claims_path=CLAIMS_CSV):
    """Return a list of error messages; empty means everything passes."""
    companies, errors = _read(Path(companies_path), COMPANY_COLUMNS)
    errors += check_companies(companies, Path(companies_path).name)
    claims_path = Path(claims_path)
    if claims_path.exists():
        claims, read_errors = _read(claims_path, CLAIM_COLUMNS)
        errors += read_errors
        errors += check_claims(claims, [c["name"] for c in companies], claims_path.name)
    return errors


def main():
    errors = check_files()
    if errors:
        print(f"{len(errors)} problem(s) found:")
        for e in errors:
            print(f"  - {e}")
        raise SystemExit(1)
    note = "" if CLAIMS_CSV.exists() else " (no claims.csv yet, so no claims were checked)"
    print(f"All checks passed{note}.")


if __name__ == "__main__":
    main()
