"""Find each Portfolio company's Original logo on its own homepage, into site/logos/.

Only the company's own site is used (never the Firm's portfolio page; see ADR 0004).
Every logo records where it came from in companies.csv (logo_origin, logo_source).
"""
import csv
import re
import struct
import unicodedata
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

EXTENSIONS = {
    "image/svg+xml": "svg",
    "image/png": "png",
    "image/jpeg": "jpg",
    "image/webp": "webp",
    "image/gif": "gif",
}
MIN_PNG_SIZE = 128
COLUMNS = ["name", "website", "fund", "is_highlight", "is_exit", "logo", "logo_background", "logo_origin", "logo_source", "researched_on"]
KEPT_ORIGINS = ("manual", "web-search")


def slugify(name):
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_name.lower()).strip("-")


def logo_filename(name, content_type):
    extension = EXTENSIONS[content_type.split(";")[0].strip().lower()]
    return f"{slugify(name)}.{extension}"


@dataclass(frozen=True)
class Logo:
    filename: str
    data: bytes
    source: str


class _Candidates(HTMLParser):
    """Collect logo candidates: header logo images, SVG icon links, apple-touch-icons."""

    def __init__(self):
        super().__init__()
        self.header_depth = 0
        self.header_imgs, self.svg_icons, self.touch_icons = [], [], []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "header":
            self.header_depth += 1
        elif tag == "img" and self.header_depth and a.get("src"):
            if any("logo" in a.get(k, "").lower() for k in ("class", "alt", "src")):
                self.header_imgs.append(a["src"])
        elif tag == "link" and a.get("href"):
            rel = a.get("rel", "").lower().split()
            href_path = a["href"].lower().split("?")[0]
            if "apple-touch-icon" in rel:
                self.touch_icons.append(a["href"])
            elif "icon" in rel and (a.get("type") == "image/svg+xml" or href_path.endswith(".svg")):
                self.svg_icons.append(a["href"])

    def handle_endtag(self, tag):
        if tag == "header" and self.header_depth:
            self.header_depth -= 1


def _homepage_candidates(website, fetch):
    try:
        data, _ = fetch(website)
    except OSError:
        return []
    parser = _Candidates()
    parser.feed(data.decode("utf-8", "ignore"))
    hrefs = parser.header_imgs + parser.svg_icons + parser.touch_icons
    return [urljoin(website, href) for href in hrefs]


def _png_size(data):
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR" or len(data) < 24:
        return None
    return struct.unpack(">II", data[16:24])


def _usable_image(url, fetch):
    """(data, content_type) if the URL is an SVG or a PNG of at least 128 px, else None."""
    try:
        data, content_type = fetch(url)
    except OSError:
        return None
    kind = content_type.split(";")[0].strip().lower()
    if kind == "image/svg+xml":
        return data, kind
    if kind == "image/png":
        size = _png_size(data)
        if size and min(size) >= MIN_PNG_SIZE:
            return data, kind
    return None


def find_logo(name, website, fetch):
    """The first usable logo on the company's own homepage, or None."""
    for url in _homepage_candidates(website, fetch):
        found = _usable_image(url, fetch)
        if found:
            return Logo(logo_filename(name, found[1]), found[0], url)
    return None


def needs_fetch(row, file_exists):
    """Re-runs keep manual/web-search rows and company-site rows whose file is present."""
    if not row["logo"]:
        return True
    origin = row.get("logo_origin", "")
    if origin in KEPT_ORIGINS:
        return False
    if origin == "company-site":
        return not file_exists
    return True  # legacy (Norte-derived): no origin recorded


def build_logo_report(rows):
    lines = ["Logo origins:"]
    lines += [f"  {r['name']}: {r['logo_origin']} ({r['logo_source']})" for r in rows if r["logo"]]
    missing = [r["name"] for r in rows if not r["logo"]]
    if missing:
        lines.append(f"Manual follow-up ({len(missing)}): no logo yet")
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


def resolve_row(row, root, fetch):
    """Update one CSV row in place, writing or deleting logo files as needed."""
    logo_path = root / row["logo"] if row["logo"] else None
    if not needs_fetch(row, bool(logo_path and logo_path.is_file())):
        return
    logo = find_logo(row["name"], row["website"], fetch)
    if logo:
        if logo_path and logo_path.is_file() and logo_path.name != logo.filename:
            logo_path.unlink()
        (root / "site" / "logos").mkdir(parents=True, exist_ok=True)
        (root / "site" / "logos" / logo.filename).write_bytes(logo.data)
        row.update(logo=f"site/logos/{logo.filename}", logo_background="", logo_origin="company-site", logo_source=logo.source)
    else:
        if logo_path and logo_path.is_file():
            logo_path.unlink()
        row.update(logo="", logo_background="", logo_origin="", logo_source="")


def main():
    with COMPANIES_CSV.open(newline="", encoding="utf-8-sig") as f:
        rows = [{c: (r.get(c) or "") for c in COLUMNS} for r in csv.DictReader(f)]
    for row in rows:
        resolve_row(row, ROOT, fetch)
    with COMPANIES_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(build_logo_report(rows))


if __name__ == "__main__":
    main()
