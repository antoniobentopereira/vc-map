import struct
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import tempfile  # noqa: E402

from fetch_logos import build_logo_report, find_logo, logo_filename, needs_fetch, resolve_row  # noqa: E402


class LogoFilenameTest(unittest.TestCase):
    def test_is_slug_of_name_plus_extension_from_content_type(self):
        self.assertEqual(logo_filename("NG.CASH", "image/svg+xml"), "ng-cash.svg")
        self.assertEqual(logo_filename("Cred Aluga!", "image/png; charset=x"), "cred-aluga.png")

    def test_is_stable_regardless_of_case_and_accents(self):
        self.assertEqual(logo_filename("Açaí Pay", "image/jpeg"), logo_filename("AÇAÍ PAY", "image/jpeg"))


def png(width, height=None):
    height = height or width
    header = b"\x89PNG\r\n\x1a\n" + struct.pack(">I", 13) + b"IHDR" + struct.pack(">II", width, height) + b"x" * 9
    return header, "image/png"


SVG = (b"<svg xmlns='http://www.w3.org/2000/svg'/>", "image/svg+xml")


def fake_web(pages):
    def fetch(url):
        if url not in pages:
            raise OSError(f"404 {url}")
        return pages[url]

    return fetch


def page(body):
    return (f"<html><head>{body}</head></html>".encode(), "text/html")


SITE = "https://alpha.com"


def find(pages):
    return find_logo("Alpha", SITE, fake_web(pages))


class FindLogoTest(unittest.TestCase):
    def test_header_img_with_logo_in_src_class_or_alt(self):
        cases = [
            ('src="/img/logo.svg"', "https://alpha.com/img/logo.svg"),
            ('class="site-logo" src="/a.svg"', "https://alpha.com/a.svg"),
            ('alt="Alpha logo" src="/b.svg"', "https://alpha.com/b.svg"),
        ]
        for attrs, src in cases:
            html = page(f"<header><a><img {attrs}></a></header>")
            logo = find({SITE: html, src: SVG})
            self.assertEqual((logo.filename, logo.source), ("alpha.svg", src), attrs)

    def test_ignores_logo_images_outside_the_header(self):
        html = page('<main><img src="/logo.svg"></main>')
        self.assertIsNone(find({SITE: html, "https://alpha.com/logo.svg": SVG}))

    def test_svg_icon_link_when_no_header_img(self):
        html = page('<link rel="icon" type="image/svg+xml" href="/i.svg">')
        self.assertEqual(find({SITE: html, "https://alpha.com/i.svg": SVG}).source, "https://alpha.com/i.svg")

    def test_apple_touch_icon_last_resort(self):
        html = page('<link rel="apple-touch-icon" href="/t.png">')
        self.assertEqual(find({SITE: html, "https://alpha.com/t.png": png(180)}).filename, "alpha.png")

    def test_header_img_beats_icons(self):
        html = page('<link rel="apple-touch-icon" href="/t.png"><body><header><img src="/logo.svg"></header></body>')
        web = {SITE: html, "https://alpha.com/logo.svg": SVG, "https://alpha.com/t.png": png(180)}
        self.assertEqual(find(web).source, "https://alpha.com/logo.svg")

    def test_never_uses_og_image_ico_or_plain_favicon(self):
        html = page(
            '<meta property="og:image" content="/og.png"><link rel="icon" href="/f.ico">'
            '<link rel="shortcut icon" href="/f.png">'
        )
        web = {
            SITE: html,
            "https://alpha.com/og.png": png(600),
            "https://alpha.com/f.ico": (b"i", "image/x-icon"),
            "https://alpha.com/f.png": png(256),
        }
        self.assertIsNone(find(web))

    def test_rejects_png_under_128px_and_tries_next_candidate(self):
        html = page('<header><img src="/logo.png"></header><link rel="apple-touch-icon" href="/t.png">')
        web = {SITE: html, "https://alpha.com/logo.png": png(64), "https://alpha.com/t.png": png(180)}
        self.assertEqual(find(web).source, "https://alpha.com/t.png")

    def test_rejects_non_svg_non_png_and_non_images(self):
        html = page('<header><img src="/logo.jpg"><img src="/logo2.png"></header>')
        web = {SITE: html, "https://alpha.com/logo.jpg": (b"j", "image/jpeg"), "https://alpha.com/logo2.png": page("")}
        self.assertIsNone(find(web))

    def test_none_when_site_unreachable(self):
        self.assertIsNone(find({}))


def row(**kw):
    base = {"name": "Alpha", "logo": "site/logos/alpha.svg", "logo_background": "dark", "logo_origin": "", "logo_source": ""}
    return {**base, **kw}


class NeedsFetchTest(unittest.TestCase):
    def test_legacy_row_without_origin_is_refetched_even_if_file_exists(self):
        self.assertTrue(needs_fetch(row(), file_exists=True))

    def test_empty_logo_is_fetched(self):
        self.assertTrue(needs_fetch(row(logo=""), file_exists=False))

    def test_manual_and_web_search_are_kept_even_with_missing_file(self):
        for origin in ("manual", "web-search"):
            self.assertFalse(needs_fetch(row(logo_origin=origin, logo_source="https://x.com"), file_exists=False))

    def test_company_site_kept_unless_file_missing(self):
        r = row(logo_origin="company-site", logo_source="https://alpha.com/l.svg")
        self.assertFalse(needs_fetch(r, file_exists=True))
        self.assertTrue(needs_fetch(r, file_exists=False))


class ResolveRowTest(unittest.TestCase):
    def legacy(self, root):
        (root / "site" / "logos").mkdir(parents=True)
        (root / "site" / "logos" / "alpha.svg").write_bytes(b"norte")
        return row(website=SITE)

    def test_legacy_logo_with_nothing_found_is_deleted_and_cleared(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            r = self.legacy(root)
            resolve_row(r, root, fake_web({}))
            self.assertEqual((r["logo"], r["logo_origin"], r["logo_source"]), ("", "", ""))
            self.assertFalse((root / "site" / "logos" / "alpha.svg").exists())

    def test_legacy_logo_is_replaced_and_second_run_changes_nothing(self):
        web = fake_web({SITE: page('<header><img src="/logo.svg"></header>'), "https://alpha.com/logo.svg": SVG})
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            r = self.legacy(root)
            resolve_row(r, root, web)
            self.assertEqual(
                (r["logo"], r["logo_origin"], r["logo_source"]),
                ("site/logos/alpha.svg", "company-site", "https://alpha.com/logo.svg"),
            )
            self.assertEqual((root / r["logo"]).read_bytes(), SVG[0])
            before = dict(r)
            resolve_row(r, root, fake_web({}))
            self.assertEqual(r, before)
            self.assertTrue((root / r["logo"]).exists())


class ReportTest(unittest.TestCase):
    def test_lists_origin_per_company_and_companies_without_logo_separately(self):
        rows = [
            row(logo_origin="company-site", logo_source="https://alpha.com/l.svg"),
            row(name="Beta", logo=""),
        ]
        report = build_logo_report(rows)
        self.assertIn("Alpha: company-site", report)
        self.assertIn("Manual follow-up (1):", report)
        self.assertIn("Beta", report.split("Manual follow-up")[1])
        self.assertNotIn("Alpha", report.split("Manual follow-up")[1])

    def test_says_so_when_every_company_has_a_logo(self):
        rows = [row(logo_origin="manual", logo_source="https://x.com")]
        self.assertIn("Every company has a logo.", build_logo_report(rows))


if __name__ == "__main__":
    unittest.main()
