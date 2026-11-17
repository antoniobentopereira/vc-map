"""Download one logo file per Portfolio company into site/logos/."""
import csv
import re
import urllib.request
from pathlib import Path
from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import urljoin

from build_roster import PORTFOLIO_URL, Company, RosterError, parse_portfolio
import unicodedata

EXTENSIONS = {
    "image/svg+xml": "svg",
    "image/png": "png",
    "image/jpeg": "jpg",
    "image/webp": "webp",
    "image/gif": "gif",
    "image/x-icon": "ico",
    "image/vnd.microsoft.icon": "ico",
}


def slugify(name):
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_name.lower()).strip("-")


def logo_filename(name, content_type):
    extension = EXTENSIONS[content_type.split(";")[0].strip().lower()]
    return f"{slugify(name)}.{extension}"


PORTFOLIO_BASE = "https://www.norte.ventures"


@dataclass(frozen=True)
class Logo:
    filename: str
    data: bytes
    source: str


class _ImageLinks(HTMLParser):
    """Collect logo candidates from a page: og:image first, then icons."""

    def __init__(self):
        super().__init__()
        self.og, self.icons = [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta" and a.get("property") == "og:image" and a.get("content"):
            self.og.append(a["content"])
        elif tag == "link" and a.get("href"):
            rel = (a.get("rel") or "").lower().split()
            if "apple-touch-icon" in rel or "icon" in rel:
                self.icons.append(a["href"])


def _site_candidates(website, fetch):
    try:
        data, _ = fetch(website)
    except OSError:
        return []
    parser = _ImageLinks()
    parser.feed(data.decode("utf-8", "ignore"))
    return [urljoin(website, href) for href in parser.og + parser.icons]


def _try_image(url, fetch):
    try:
        data, content_type = fetch(url)
    except OSError:
        return None
    if content_type.split(";")[0].strip().lower() not in EXTENSIONS:
        return None
    return data, content_type


def find_logo(company, fetch):
    """Try the portfolio page, then the company's own site. None if both fail."""
    if company.logo_url:
        url = urljoin(PORTFOLIO_BASE, company.logo_url)
        found = _try_image(url, fetch)
        if found:
            return Logo(logo_filename(company.name, found[1]), found[0], "portfolio page")
    for url in _site_candidates(company.website, fetch):
        found = _try_image(url, fetch)
        if found:
            return Logo(logo_filename(company.name, found[1]), found[0], f"company site: {url}")
    return None


def build_logo_report(results):
    """results: list of (company, Logo | None)."""
    lines = ["Logo sources:"]
    lines += [f"  {c.name}: {l.filename} ({l.source})" for c, l in results if l]
    missing = [c.name for c, l in results if not l]
    if missing:
        lines.append(f"No logo found ({len(missing)}):")
        lines += [f"  {name}" for name in missing]
    else:
        lines.append("Every company has a logo.")
    return "\n".join(lines)


ROOT = Path(__file__).resolve().parent.parent
LOGO_DIR = ROOT / "site" / "logos"
COMPANIES_CSV = ROOT / "data" / "companies.csv"


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read(), response.headers.get("Content-Type", "")


def main():
    with COMPANIES_CSV.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    try:
        portfolio = {c.name.casefold(): c for c in parse_portfolio(fetch(PORTFOLIO_URL)[0].decode("utf-8"))}
    except (RosterError, OSError) as error:
        raise SystemExit(f"Could not read the portfolio page: {error}")
    LOGO_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    for row in rows:
        company = portfolio.get(row["name"].casefold()) or Company(
            row["name"], row["website"], row["fund"], False, False
        )
        existing = ROOT / row.get("logo", "") if row.get("logo") else None
        if existing and existing.is_file():  # keep logos already collected, including hand-added ones
            results.append((company, Logo(existing.name, b"", "already present")))
            continue
        logo = find_logo(company, fetch)
        if logo:
            (LOGO_DIR / logo.filename).write_bytes(logo.data)
            row["logo"] = f"site/logos/{logo.filename}"
        results.append((company, logo))
    with COMPANIES_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "website", "fund", "is_highlight", "is_exit", "logo"])
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") or "" for k in writer.fieldnames})
    print(build_logo_report(results))


if __name__ == "__main__":
    main()
