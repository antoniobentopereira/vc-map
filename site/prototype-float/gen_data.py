"""PROTOTYPE, throwaway. Reads data/companies.csv once and writes the minimal
JSON the Float prototype needs (name, logo file, fund, logo background).
This is NOT the real site JSON (that one carries value/Basis/Confidence/Source)."""
import csv, json, os
from pathlib import Path

repo = Path(__file__).resolve().parents[2]
rows = csv.DictReader(open(repo / "data" / "companies.csv", encoding="utf-8"))
out = [
    {
        "name": r["name"],
        "logo": os.path.basename(r["logo"]),
        "fund": r["fund"],
        "bg": r["logo_background"],
    }
    for r in rows
]
dest = Path(__file__).parent / "src" / "companies.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {len(out)} companies to {dest}")
