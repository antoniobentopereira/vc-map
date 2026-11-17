import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from build_roster import Company, build_report, parse_portfolio  # noqa: E402


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
                Company("Alpha", "https://alpha.com", "I", False, False),
                Company("Beta", "https://beta.com", "II", True, False),
                Company("Gamma", "https://gamma.com", "I", False, True),
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
            [Company("Alpha", "https://alpha.com", "I", True, False)],
        )


class BuildReportTest(unittest.TestCase):
    def test_states_total_count(self):
        companies = [
            Company("Alpha", "https://alpha.com", "I", False, False),
            Company("Beta", "https://beta.com", "II", False, False),
        ]
        self.assertIn("Total companies: 2", build_report(companies))

    def test_lists_company_in_both_funds_without_merging(self):
        companies = [
            Company("Alpha", "https://alpha.com", "I", False, False),
            Company("Alpha", "https://alpha.com", "II", False, False),
            Company("Beta", "https://beta.com", "II", False, False),
        ]
        report = build_report(companies)
        self.assertIn("Alpha (Fund I, Fund II)", report)
        self.assertNotIn("Beta (", report)
        self.assertIn("Total companies: 3", report)

    def test_says_so_when_no_company_is_in_both_funds(self):
        companies = [Company("Beta", "https://beta.com", "II", False, False)]
        self.assertIn("No company appears in more than one Fund", build_report(companies))


if __name__ == "__main__":
    unittest.main()
