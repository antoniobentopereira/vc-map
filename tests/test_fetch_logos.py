import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from build_roster import Company  # noqa: E402
from fetch_logos import Logo, build_logo_report, find_logo, logo_filename  # noqa: E402


class LogoFilenameTest(unittest.TestCase):
    def test_is_slug_of_name_plus_extension_from_content_type(self):
        self.assertEqual(logo_filename("NG.CASH", "image/svg+xml"), "ng-cash.svg")
        self.assertEqual(logo_filename("Cred Aluga!", "image/png; charset=x"), "cred-aluga.png")

    def test_is_stable_regardless_of_case_and_accents(self):
        self.assertEqual(logo_filename("Açaí Pay", "image/jpeg"), logo_filename("AÇAÍ PAY", "image/jpeg"))
        self.assertEqual(logo_filename("Açaí Pay", "image/jpeg"), "acai-pay.jpg")


def fake_web(pages):
    """A fetch(url) -> (bytes, content_type) backed by a dict; misses raise OSError."""

    def fetch(url):
        if url not in pages:
            raise OSError(f"404 {url}")
        return pages[url]

    return fetch


ALPHA = Company("Alpha", "https://alpha.com", "I", False, False, "/api/media/file/alpha.svg")
PNG = (b"png-bytes", "image/png")
SVG = (b"svg-bytes", "image/svg+xml")


def html(body):
    return (f"<html><head>{body}</head></html>".encode(), "text/html")


class FindLogoTest(unittest.TestCase):
    def test_prefers_the_official_portfolio_page(self):
        web = fake_web({"https://www.norte.ventures/api/media/file/alpha.svg": SVG})
        logo = find_logo(ALPHA, web)
        self.assertEqual((logo.filename, logo.data, logo.source), ("alpha.svg", b"svg-bytes", "portfolio page"))

    def test_falls_back_to_company_site_og_image(self):
        web = fake_web(
            {
                "https://alpha.com": html('<meta property="og:image" content="/img/logo.png">'),
                "https://alpha.com/img/logo.png": PNG,
            }
        )
        logo = find_logo(ALPHA, web)
        self.assertEqual((logo.filename, logo.source), ("alpha.png", "company site: https://alpha.com/img/logo.png"))

    def test_falls_back_to_company_site_icon_when_no_og_image(self):
        web = fake_web(
            {
                "https://alpha.com": html('<link rel="apple-touch-icon" href="https://cdn.x/icon.png">'),
                "https://cdn.x/icon.png": PNG,
            }
        )
        self.assertEqual(find_logo(ALPHA, web).source, "company site: https://cdn.x/icon.png")

    def test_skips_a_portfolio_logo_that_is_not_an_image(self):
        web = fake_web(
            {
                "https://www.norte.ventures/api/media/file/alpha.svg": html(""),
                "https://alpha.com": html('<meta property="og:image" content="/l.png">'),
                "https://alpha.com/l.png": PNG,
            }
        )
        self.assertTrue(find_logo(ALPHA, web).source.startswith("company site"))

    def test_returns_none_when_nothing_is_found(self):
        self.assertIsNone(find_logo(ALPHA, fake_web({})))


class ReportTest(unittest.TestCase):
    def test_lists_each_logo_source_and_names_companies_without_a_logo(self):
        beta = Company("Beta", "https://beta.com", "II", False, False)
        report = build_logo_report(
            [(ALPHA, Logo("alpha.svg", b"", "portfolio page")), (beta, None)]
        )
        self.assertIn("Alpha: alpha.svg (portfolio page)", report)
        self.assertIn("No logo found (1):", report)
        self.assertIn("Beta", report.split("No logo found")[1])
        self.assertNotIn("Alpha", report.split("No logo found")[1])

    def test_says_so_when_every_company_has_a_logo(self):
        report = build_logo_report([(ALPHA, Logo("alpha.svg", b"", "portfolio page"))])
        self.assertIn("Every company has a logo.", report)


if __name__ == "__main__":
    unittest.main()
