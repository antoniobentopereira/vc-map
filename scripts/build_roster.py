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


class RosterError(Exception):
    """The page's Fund data needs a human decision; nothing is written."""


@dataclass(frozen=True)
class Company:
    name: str
    website: str
    fund: str
    is_highlight: bool
    is_exit: bool
    logo_url: str = ""


def _flight_text(html):
    chunks = re.findall(r"self\.__next_f\.push\((\[.*?\])\)</script>", html, re.S)
    return "".join(json.loads(c)[1] for c in chunks)


def parse_portfolio(html):
    text = _flight_text(html)
    start = text.index('"companies":[') + len('"companies":')
    entries, _ = json.JSONDecoder().raw_decode(text, start)
    companies = {}
    problems = []
    funds_seen = {}
    for e in entries:
        slugs = [c["slug"] for c in e["majorCategories"]]
        funds = sorted({FUND_BY_SLUG[s] for s in slugs if s in FUND_BY_SLUG})
        if not funds:
            problems.append(f"{e['name']}: no Fund tag (needs Fund I or Fund II)")
            continue
        funds_seen.setdefault(e["name"].casefold(), (e["name"], set()))[1].update(funds)
        if len(funds) > 1:
            continue
        key = (e["name"].casefold(), funds[0])
        previous = companies.get(key)
        companies[key] = Company(
            name=e["name"].strip(),
            website=e["url"],
            fund=funds[0],
            is_highlight="highlights" in slugs or bool(previous and previous.is_highlight),
            is_exit="exit" in slugs or bool(previous and previous.is_exit),
            logo_url=(e.get("image") or {}).get("url", ""),
        )
    for name, funds in funds_seen.values():
        if len(funds) > 1:
            problems.append(f"{name}: appears in both Fund I and Fund II")
    if problems:
        raise RosterError(
            "The portfolio page needs a decision before the roster can be built:\n"
            + "\n".join(f"  - {p}" for p in problems)
        )
    return list(companies.values())


def build_report(companies):
    return f"Total companies: {len(companies)}"


def fetch(url=PORTFOLIO_URL):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


# Columns filled by later steps (logos, research), kept as they are when the roster is rebuilt.
KEPT_COLUMNS = ["logo", "logo_background", "logo_origin", "logo_source", "researched_on"]


def _existing_kept_columns(path):
    """Columns filled by later steps already in the CSV, so rebuilding the roster does not erase them."""
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8-sig") as f:
        return {r["name"].casefold(): [r.get(c, "") or "" for c in KEPT_COLUMNS] for r in csv.DictReader(f)}


def write_csv(companies, path=OUTPUT):
    path.parent.mkdir(parents=True, exist_ok=True)
    kept = _existing_kept_columns(path)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "website", "fund", "is_highlight", "is_exit", *KEPT_COLUMNS])
        for c in companies:
            writer.writerow(
                [c.name, c.website, c.fund, str(c.is_highlight).upper(), str(c.is_exit).upper(),
                 *kept.get(c.name.casefold(), [""] * len(KEPT_COLUMNS))]
            )


def main():
    try:
        companies = parse_portfolio(fetch())
    except RosterError as error:
        raise SystemExit(f"{error}\nNo file was written.")
    write_csv(companies)
    print(build_report(companies))
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
