import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from build_site_data import build  # noqa: E402
from test_check_data import ALPHA, HEADER, HEADERS, touch_logos, write  # noqa: E402


def make_data(directory, companies):
    lines = [HEADER, *companies]
    touch_logos(directory, lines)
    write(directory, "companies.csv", lines)
    for name in ("claims", "rounds", "fx", "sectors"):
        write(directory, f"{name}.csv", [HEADERS[name]])


BETA = "Beta Co.,https://beta.com,II,TRUE,FALSE,site/logos/beta.png,,company-site,https://beta.com/logo.png,"


class BuildSiteDataTest(unittest.TestCase):
    def build(self, companies):
        with tempfile.TemporaryDirectory() as d:
            make_data(d, companies)
            return build(d, d)

    def test_one_entry_per_company_with_slug_name_fund_and_site_relative_logo(self):
        data = self.build([ALPHA, BETA])
        self.assertEqual(
            [(c["slug"], c["name"], c["fund"], c["logo"]) for c in data["companies"]],
            [("alpha", "Alpha", "I", "logos/alpha.svg"), ("beta-co", "Beta Co.", "II", "logos/beta.png")],
        )

    def test_website_comes_from_the_roster(self):
        self.assertEqual([c["website"] for c in self.build([ALPHA, BETA])["companies"]], ["https://alpha.com", "https://beta.com"])

    def test_slugs_are_ascii_and_unique(self):
        accents = BETA.replace("Beta Co.", "Açaí & Café!").replace("beta.png", "cafe.png")
        self.assertEqual(self.build([accents])["companies"][0]["slug"], "acai-cafe")
        twin = BETA.replace("Beta Co.", "beta co").replace("beta.png", "beta2.png")
        slugs = [c["slug"] for c in self.build([BETA, twin])["companies"]]
        self.assertEqual(slugs, ["beta-co", "beta-co-2"])

    def build_with(self, companies, claims, sectors=()):
        with tempfile.TemporaryDirectory() as d:
            make_data(d, companies)
            write(d, "claims.csv", [HEADERS["claims"], *claims])
            write(d, "sectors.csv", [HEADERS["sectors"], *sectors])
            return build(d, d)["companies"][0]

    def test_card_fields_carry_value_basis_confidence_and_source(self):
        company = self.build_with(
            [ALPHA],
            [
                "Alpha,description,Makes alphas.,https://alpha.com/about,reported,high,",
                "Alpha,year_founded,2019,https://alpha.com/about,estimated,low,Registry date.",
            ],
        )
        self.assertEqual(
            company["fields"]["description"],
            {"value": "Makes alphas.", "basis": "reported", "confidence": "high", "source": "https://alpha.com/about"},
        )
        self.assertEqual(
            company["fields"]["year_founded"],
            {"value": 2019, "basis": "estimated", "confidence": "low", "source": "https://alpha.com/about"},
        )

    def test_sector_comes_from_the_mapping_and_keeps_the_sub_sector_claim_provenance(self):
        company = self.build_with(
            [ALPHA],
            ["Alpha,sub_sector,Fraud scoring,https://alpha.com/about,estimated,medium,Guess."],
            ["Fraud scoring,Security & Fraud"],
        )
        self.assertEqual(
            company["fields"]["sector"],
            {"value": "Security & Fraud", "basis": "estimated", "confidence": "medium", "source": "https://alpha.com/about"},
        )

    def test_missing_fields_are_absent(self):
        company = self.build_with([ALPHA], [])
        self.assertEqual(company["fields"], {})

    def test_refuses_to_build_when_the_check_fails(self):
        with tempfile.TemporaryDirectory() as d:
            make_data(d, [ALPHA.replace("site/logos/alpha.svg", "site/logos/missing.svg")])
            (Path(d) / "site/logos/missing.svg").unlink()
            with self.assertRaises(SystemExit):
                build(d, d)


if __name__ == "__main__":
    unittest.main()
