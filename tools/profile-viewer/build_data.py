"""Generate tools/profile-viewer/data.js from the CSVs in data/ (read-only; see ADR 0008).

Usage: python tools/profile-viewer/build_data.py
The page loads data.js as a script, because a file:// page cannot fetch CSVs.
"""
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DATA = ROOT / "data"
OUTPUT = HERE / "data.js"


def read(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build():
    companies = read("companies.csv")
    sectors = {r["sub_sector"]: r["sector"] for r in read("sectors.csv")}

    rows_by_company = {}
    for kind in ("claims", "rounds"):
        for row in read(f"{kind}.csv"):
            rows_by_company.setdefault(row["company"], {"claims": [], "rounds": []})[kind].append(row)

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
            "claims": rows["claims"],
            "rounds": rows["rounds"],
        })
    return {"profiles": profiles, "sectors": sectors}


def main():
    data = build()
    OUTPUT.write_text("window.PROFILE_DATA = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n",
                      encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}: {len(data['profiles'])} companies")


if __name__ == "__main__":
    sys.exit(main())
