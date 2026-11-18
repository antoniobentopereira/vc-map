import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from build_roster import Company, RosterError, build_report, parse_portfolio, write_csv  # noqa: E402


def make_page(companies):
    """Build HTML shaped like the real portfolio page: the company list sits
    inside Next.js flight data pushed through self.__next_f.push."""
    payload = '0:["x",{"companies":' + json.dumps(companies) + ',"other":1}]'
    push = json.dumps([1, payload])
    return f"<html><body><script>self.__next_f.push({push})</script></body></html>"


def entry(name, url, *tags):
    return {
        "id": name,
        "name": name,
        "image": {"url": f"/api/media/file/{name.lower()}.svg"},
        "url": url,
        "majorCategories": [{"id": t, "slug": t} for t in tags],
        "subCategories": [{"id": "f", "slug": "fintech"}],
    }


def LOGO(name):
    return f"/api/media/file/{name.lower()}.svg"


class ParsePortfolioTest(unittest.TestCase):
    def test_reads_name_website_fund_and_flags(self):
        html = make_page(
            [
                entry("Alpha", "https://alpha.com", "fund-1"),
                entry("Beta", "https://beta.com", "fund-2", "highlights"),
                entry("Gamma", "https://gamma.com", "fund-1", "exit"),
            ]
        )
        self.assertEqual(
            parse_portfolio(html),
            [
                Company("Alpha", "https://alpha.com", "I", False, False, LOGO("Alpha")),
                Company("Beta", "https://beta.com", "II", True, False, LOGO("Beta")),
                Company("Gamma", "https://gamma.com", "I", False, True, LOGO("Gamma")),
            ],
        )

    def test_company_repeated_in_same_fund_appears_once(self):
        html = make_page(
            [
                entry("Alpha", "https://alpha.com", "fund-1"),
                entry("Alpha", "https://alpha.com", "fund-1", "highlights"),
            ]
        )
        self.assertEqual(
            parse_portfolio(html),
            [Company("Alpha", "https://alpha.com", "I", True, False, LOGO("Alpha"))],
        )


class FundProblemsTest(unittest.TestCase):
    def parse_error(self, companies):
        with self.assertRaises(RosterError) as ctx:
            parse_portfolio(make_page(companies))
        return str(ctx.exception)

    def test_entry_tagged_with_both_funds_stops_with_clear_error(self):
        message = self.parse_error(
            [
                entry("Alpha", "https://alpha.com", "fund-1", "fund-2"),
                entry("Beta", "https://beta.com", "fund-2"),
            ]
        )
        self.assertIn("Alpha", message)
        self.assertIn("both Fund I and Fund II", message)
        self.assertNotIn("Beta", message)

    def test_company_listed_separately_in_both_funds_stops_with_clear_error(self):
        message = self.parse_error(
            [
                entry("Alpha", "https://alpha.com", "fund-1"),
                entry("Alpha", "https://alpha.com", "fund-2"),
            ]
        )
        self.assertIn("Alpha", message)
        self.assertIn("both Fund I and Fund II", message)

    def test_entry_with_no_fund_stops_with_clear_error(self):
        message = self.parse_error(
            [
                entry("Gamma", "https://gamma.com", "highlights"),
                entry("Beta", "https://beta.com", "fund-2"),
            ]
        )
        self.assertIn("Gamma", message)
        self.assertIn("no Fund", message)
        self.assertNotIn("Beta", message)

    def test_reports_every_problem_at_once(self):
        message = self.parse_error(
            [
                entry("Alpha", "https://alpha.com", "fund-1", "fund-2"),
                entry("Gamma", "https://gamma.com"),
            ]
        )
        self.assertIn("Alpha", message)
        self.assertIn("Gamma", message)


class BuildReportTest(unittest.TestCase):
    def test_states_total_count(self):
        companies = [
            Company("Alpha", "https://alpha.com", "I", False, False, LOGO("Alpha")),
            Company("Beta", "https://beta.com", "II", False, False),
        ]
        self.assertIn("Total companies: 2", build_report(companies))


class WriteCsvTest(unittest.TestCase):
    def test_rebuilding_keeps_logo_and_researched_on_columns(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "companies.csv"
            path.write_text(
                "name,website,fund,is_highlight,is_exit,logo,logo_origin,logo_source,researched_on\n"
                "Alpha,https://a.com,I,FALSE,FALSE,site/logos/a.svg,manual,https://a.com/l.svg,2026-11-18\n",
                encoding="utf-8",
            )
            write_csv([Company("Alpha", "https://a.com", "II", True, False),
                       Company("Beta", "https://b.com", "I", False, False)], path)
            lines = path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(lines, [
            "name,website,fund,is_highlight,is_exit,logo,logo_origin,logo_source,researched_on",
            "Alpha,https://a.com,II,TRUE,FALSE,site/logos/a.svg,manual,https://a.com/l.svg,2026-11-18",
            "Beta,https://b.com,I,FALSE,FALSE,,,,",
        ])


if __name__ == "__main__":
    unittest.main()
