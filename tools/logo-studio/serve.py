"""Local logo studio: crop, pick the fill, preview and confirm each logo's circle (ADR 0015).

Usage: python tools/logo-studio/serve.py   (then open http://localhost:8765)
Disposable (ADR 0008): writes only the `logo_crop` and `logo_background` columns of data/companies.csv
and the logo circle files, through scripts/logo_circle.py. Nothing under site/ is changed except the circles.
"""
import csv
import json
import os
import sys
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_data import COMPANIES_CSV, COMPANY_COLUMNS, LOGO_COLOR, _is_crop  # noqa: E402
from logo_circle import circle_path, open_logo, parse_crop, render_circle, save_circle  # noqa: E402

PORT = 8765
IMAGE_TYPES = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp",
               ".gif": "image/gif"}


def read_rows(path=COMPANIES_CSV):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def save_choice(name, crop, background, path=COMPANIES_CSV, root=ROOT):
    """Save one company's crop (`x,y,w,h` fractions, or "" for the whole image) and `#rrggbb` fill, then render its circle.

    Raises ValueError, leaving the CSV untouched, when the input is invalid or the logo cannot be rendered.
    Changes no column other than logo_crop and logo_background."""
    if not LOGO_COLOR.fullmatch(background):
        raise ValueError(f"fill '{background}' must be #rrggbb")
    if crop and not _is_crop(crop):
        raise ValueError(f"crop '{crop}' must be four fractions from 0 to 1 as x,y,w,h")
    rows = read_rows(path)
    target = next((r for r in rows if r["name"] == name and r["logo"]), None)
    if target is None:
        raise ValueError(f"no company '{name}' with a logo")
    try:  # render first: a logo that cannot render must not leave a choice saved
        circle = render_circle(open_logo(Path(root) / target["logo"]), parse_crop(crop), background)
    except Exception as error:
        raise ValueError(f"cannot render {target['logo']}: {error}") from error
    target["logo_crop"] = crop
    target["logo_background"] = background
    fd, tmp = tempfile.mkstemp(dir=Path(path).parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=COMPANY_COLUMNS)
            writer.writeheader()
            writer.writerows(rows)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise
    save_circle(circle, Path(root) / circle_path(target["logo"]))


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/":
            self._send(200, (HERE / "index.html").read_bytes(), "text/html; charset=utf-8")
        elif path == "/api/logos":
            data = [{"name": r["name"], "logo": r["logo"], "crop": r["logo_crop"], "background": r["logo_background"]}
                    for r in read_rows() if r["logo"]]
            self._send(200, json.dumps(data).encode(), "application/json")
        elif path.startswith("/site/logos/"):
            file = (ROOT / path.lstrip("/")).resolve()
            if file.parent != (ROOT / "site" / "logos").resolve() or not file.is_file():
                return self._send(404, b"not found", "text/plain")
            self._send(200, file.read_bytes(), IMAGE_TYPES.get(file.suffix.lower(), "application/octet-stream"))
        else:
            self._send(404, b"not found", "text/plain")

    def do_POST(self):
        if self.path != "/api/save":
            return self._send(404, b"not found", "text/plain")
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
            save_choice(body["name"], body["crop"], body["background"])
            result, status = {"ok": True}, 200
        except (ValueError, KeyError, TypeError) as error:
            result, status = {"ok": False, "error": str(error)}, 400
        self._send(status, json.dumps(result).encode(), "application/json")

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"Logo studio on http://localhost:{PORT} (Ctrl+C to stop)")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
