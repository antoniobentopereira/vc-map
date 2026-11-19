"""Generate tools/profile-viewer/data.js from the CSVs in data/ (read-only; see ADR 0008).

Usage: python tools/profile-viewer/build_data.py
The page loads data.js as a script, because a file:// page cannot fetch CSVs.
"""
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
from check_data import (  # noqa: E402
    ALLOWED_BUSINESS_MODELS, ALLOWED_LOGO_ORIGINS, ALLOWED_STATUS, CLAIM_COLUMNS, COMPANY_COLUMNS, ROUND_COLUMNS,
    ROUND_TYPES, _read, check_files,
)
from derive import _order, first_investment, follow_on, last_round  # noqa: E402  (one definition of each view)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DATA = ROOT / "data"
OUTPUT = HERE / "data.js"


def read(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def check_findings():
    """Run the existing data check; return ({company: [messages]}, [dataset-wide messages]).

    check_files reports "<file> line N: ..." without the company, so each message is
    attributed through the row on that line. Messages with no line are dataset-wide.
    """
    owners = {}
    for filename, columns in (("companies.csv", COMPANY_COLUMNS), ("claims.csv", CLAIM_COLUMNS),
                              ("rounds.csv", ROUND_COLUMNS)):
        rows, _ = _read(DATA / filename, columns)
        for row in rows:
            owners[(filename, row["_line"])] = row["name" if filename == "companies.csv" else "company"]
    by_company, general = {}, []
    for message in check_files(DATA, ROOT):
        m = re.match(r"(\S+\.csv) line (\d+):", message)
        owner = owners.get((m.group(1), int(m.group(2)))) if m else None
        if owner:
            by_company.setdefault(owner, []).append(message)
        else:
            general.append(message)
    return by_company, general


def build():
    companies = read("companies.csv")
    sectors = {r["sub_sector"]: r["sector"] for r in read("sectors.csv")}

    rows_by_company = {}
    for kind in ("claims", "rounds"):
        for row in read(f"{kind}.csv"):
            rows_by_company.setdefault(row["company"], {"claims": [], "rounds": []})[kind].append(row)

    findings, general = check_findings()
    profiles = []
    for company in companies:  # roster order
        rows = rows_by_company.get(company["name"], {"claims": [], "rounds": []})
        if not (rows["claims"] or rows["rounds"] or company["researched_on"]):
            continue
        logo = company["logo"]
        profiles.append({
            "name": company["name"],
            "logo": f"../../{logo}" if logo and (ROOT / logo).is_file() else "",
            "researched_on": company["researched_on"],
            "record": {key: company[key] for key in ("website", "fund", "is_highlight", "is_exit", "logo",
                                                      "logo_origin", "logo_source")},
            "check_errors": findings.get(company["name"], []),
            "claims": rows["claims"],
            "rounds": sorted(rows["rounds"], key=_order),  # year, then stage
            "derived": {
                "first_investment": first_investment(rows["rounds"]),
                "last_round": last_round(rows["rounds"]),
                "follow_on": follow_on(rows["rounds"]),
            },
        })
    # allowed values come from the check script, so the gap templates cannot drift from the rules
    allowed = {"round_types": ROUND_TYPES, "status": ALLOWED_STATUS, "business_models": ALLOWED_BUSINESS_MODELS,
               "logo_origins": ALLOWED_LOGO_ORIGINS}
    return {"profiles": profiles, "sectors": sectors, "allowed": allowed, "check_general": general}


def main():
    data = build()
    OUTPUT.write_text("window.PROFILE_DATA = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n",
                      encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}: {len(data['profiles'])} companies")


if __name__ == "__main__":
    sys.exit(main())
