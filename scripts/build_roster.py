"""Build data/companies.csv from the official Norte Ventures portfolio page."""
import csv
import json
import re
import urllib.request
from pathlib import Path
from dataclasses import dataclass

PORTFOLIO_URL = "https://www.norte.ventures/portfolio"
OUTPUT = Path(__file__).resolve().parent.parent / "data" / "companies.csv"
FUND_BY_SLUG = {"fund-1": "I", "fund-2": "II"}


@dataclass(frozen=True)
class Company:
    name: str
    website: str
    fund: str
    is_highlight: bool
    is_exit: bool


def _flight_text(html):
    chunks = re.findall(r"self\.__next_f\.push\((\[.*?\])\)</script>", html, re.S)
    return "".join(json.loads(c)[1] for c in chunks)


def parse_portfolio(html):
    text = _flight_text(html)
    start = text.index('"companies":[') + len('"companies":')
    entries, _ = json.JSONDecoder().raw_decode(text, start)
    companies = {}
    for e in entries:
        slugs = [c["slug"] for c in e["majorCategories"]]
        fund = FUND_BY_SLUG[next(s for s in slugs if s in FUND_BY_SLUG)]
        key = (e["name"].casefold(), fund)
        previous = companies.get(key)
        companies[key] = Company(
            name=e["name"],
            website=e["url"],
            fund=fund,
            is_highlight="highlights" in slugs or bool(previous and previous.is_highlight),
            is_exit="exit" in slugs or bool(previous and previous.is_exit),
        )
    return list(companies.values())


def build_report(companies):
    funds_by_name = {}
    for c in companies:
        funds_by_name.setdefault(c.name.casefold(), (c.name, []))[1].append(c.fund)
    lines = [f"Total companies: {len(companies)}"]
    multi = [(n, f) for n, f in funds_by_name.values() if len(set(f)) > 1]
    if multi:
        lines.append("Companies in more than one Fund (not merged, resolve by hand):")
        for name, funds in multi:
            lines.append(f"  {name} ({', '.join('Fund ' + f for f in funds)})")
    else:
        lines.append("No company appears in more than one Fund.")
    return "\n".join(lines)


def fetch(url=PORTFOLIO_URL):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def write_csv(companies, path=OUTPUT):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "website", "fund", "is_highlight", "is_exit"])
        for c in companies:
            writer.writerow(
                [c.name, c.website, c.fund, str(c.is_highlight).upper(), str(c.is_exit).upper()]
            )


def main():
    companies = parse_portfolio(fetch())
    write_csv(companies)
    print(build_report(companies))
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
