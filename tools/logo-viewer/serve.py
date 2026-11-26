"""Local logo review page: each logo on a dark and a light background, saving the pick to companies.csv.

Usage: python tools/logo-viewer/serve.py   (then open http://localhost:8765)
Writes only the `logo_background` column of data/companies.csv, on every click.
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
from check_data import ALLOWED_LOGO_BACKGROUNDS, COMPANIES_CSV, COMPANY_COLUMNS  # noqa: E402

PORT = 8765
IMAGE_TYPES = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp",
               ".gif": "image/gif"}


def read_rows(path=COMPANIES_CSV):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def set_background(name, value, path=COMPANIES_CSV):
    """Set (or clear, with "") one company's logo_background; return False if the pick is not valid."""
    if value not in ALLOWED_LOGO_BACKGROUNDS and value != "":
        return False
    rows = read_rows(path)
    target = next((r for r in rows if r["name"] == name and r["logo"]), None)
    if target is None:
        return False
    target["logo_background"] = value
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COMPANY_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)
    return True


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
            data = [{"name": r["name"], "logo": r["logo"], "background": r["logo_background"]}
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
        if self.path != "/api/background":
            return self._send(404, b"not found", "text/plain")
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
            ok = set_background(body["name"], body["value"])
        except (ValueError, KeyError, TypeError):
            ok = False
        self._send(200 if ok else 400, json.dumps({"ok": ok}).encode(), "application/json")

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"Logo viewer on http://localhost:{PORT} (Ctrl+C to stop)")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
