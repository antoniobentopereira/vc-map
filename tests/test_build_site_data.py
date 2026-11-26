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

    def test_logo_points_to_the_circle_when_one_exists_and_to_the_raw_logo_otherwise(self):
        with tempfile.TemporaryDirectory() as d:
            make_data(d, [ALPHA.replace(".svg,,company-site", ".svg,#ffffff,company-site"), BETA])
            circle = Path(d) / "site" / "logos" / "circles" / "alpha.webp"
            circle.parent.mkdir(parents=True)
            circle.write_bytes(b"x")
            logos = [c["logo"] for c in build(d, d)["companies"]]
        self.assertEqual(logos, ["logos/circles/alpha.webp", "logos/beta.png"])

    def test_logo_without_a_hex_fill_keeps_the_raw_logo_even_if_a_circle_file_exists(self):
        with tempfile.TemporaryDirectory() as d:
            make_data(d, [ALPHA])  # logo_background is empty
            circle = Path(d) / "site" / "logos" / "circles" / "alpha.webp"
            circle.parent.mkdir(parents=True)
            circle.write_bytes(b"x")
            self.assertEqual(build(d, d)["companies"][0]["logo"], "logos/alpha.svg")

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

    def build_full(self, claims=(), rounds=()):
        with tempfile.TemporaryDirectory() as d:
            make_data(d, [ALPHA])
            write(d, "claims.csv", [HEADERS["claims"], *claims])
            write(d, "rounds.csv", [HEADERS["rounds"], *rounds])
            return build(d, d)["companies"][0]

    def test_profile_single_value_fields_carry_provenance(self):
        company = self.build_full(
            [
                "Alpha,long_description,A long story.,https://alpha.com/a,reported,high,",
                "Alpha,investment_thesis,Why it works.,https://alpha.com/b,estimated,medium,Deduced.",
                "Alpha,acquisition_year,2024,https://alpha.com/c,reported,high,",
                "Alpha,hq,\"Sao Paulo, Brazil\",https://alpha.com/d,reported,high,",
            ]
        )
        fields = company["fields"]
        self.assertEqual(fields["investment_thesis"], {"value": "Why it works.", "basis": "estimated", "confidence": "medium", "source": "https://alpha.com/b"})
        self.assertEqual(fields["acquisition_year"]["value"], 2024)
        self.assertEqual(fields["hq"]["value"], "Sao Paulo, Brazil")
        self.assertEqual(fields["long_description"]["value"], "A long story.")

    def test_list_fields_are_lists_of_fields_in_file_order(self):
        company = self.build_full(
            [
                "Alpha,founder,Ana,https://alpha.com/a,reported,high,",
                "Alpha,founder,Bo,https://alpha.com/b,estimated,low,Deduced.",
                "Alpha,market,Brazil,https://alpha.com/c,reported,high,",
                "Alpha,accelerator,Y Combinator,https://alpha.com/d,reported,high,",
            ]
        )
        self.assertEqual([f["value"] for f in company["lists"]["founders"]], ["Ana", "Bo"])
        self.assertEqual(company["lists"]["founders"][1], {"value": "Bo", "basis": "estimated", "confidence": "low", "source": "https://alpha.com/b"})
        self.assertEqual([f["value"] for f in company["lists"]["markets"]], ["Brazil"])
        self.assertEqual([f["value"] for f in company["lists"]["accelerators"]], ["Y Combinator"])

    def test_milestones_split_into_date_and_event_and_sort_by_date(self):
        company = self.build_full(
            [
                "Alpha,milestone,2021-03: Joined an accelerator.,https://alpha.com/a,reported,high,",
                "Alpha,milestone,2019: Founded.,https://alpha.com/b,reported,high,",
            ]
        )
        self.assertEqual(
            [(m["date"], m["value"]) for m in company["lists"]["milestones"]],
            [("2019", "Founded."), ("2021-03", "Joined an accelerator.")],
        )
        self.assertEqual(company["lists"]["milestones"][0]["source"], "https://alpha.com/b")

    def test_lists_are_empty_and_rounds_empty_when_nothing_found(self):
        company = self.build_full()
        self.assertEqual(company["lists"], {"founders": [], "markets": [], "accelerators": [], "milestones": []})
        self.assertEqual(company["rounds"], [])
        self.assertIsNone(company["first_investment"])
        self.assertIsNone(company["follow_on"])

    def test_rounds_carry_own_provenance_usd_size_and_norte_participation(self):
        company = self.build_full(
            rounds=[
                "Alpha,2022,seed,1000,USD,1000,Fund X (lead),FALSE,https://alpha.com/r1,reported,high,",
                "Alpha,2021,pre_seed,,,,,TRUE,https://alpha.com/r0,estimated,low,Deduced.",
                "Alpha,2023,series_a,,,,,UNKNOWN,https://alpha.com/r2,reported,medium,",
            ]
        )
        self.assertEqual(
            company["rounds"],
            [
                {"year": 2021, "type": "pre_seed", "size_usd": None, "norte": True, "co_investors": [],
                 "basis": "estimated", "confidence": "low", "source": "https://alpha.com/r0"},
                {"year": 2022, "type": "seed", "size_usd": 1000, "norte": False, "co_investors": ["Fund X (lead)"],
                 "basis": "reported", "confidence": "high", "source": "https://alpha.com/r1"},
                {"year": 2023, "type": "series_a", "size_usd": None, "norte": None, "co_investors": [],
                 "basis": "reported", "confidence": "medium", "source": "https://alpha.com/r2"},
            ],
        )

    def test_first_investment_and_follow_on_come_from_the_derived_views(self):
        company = self.build_full(
            rounds=[
                "Alpha,2021,seed,,,,,TRUE,https://alpha.com/r0,reported,high,",
                "Alpha,2022,series_a,,,,,TRUE,https://alpha.com/r1,reported,high,",
            ]
        )
        self.assertEqual((company["first_investment"]["year"], company["first_investment"]["type"]), (2021, "seed"))
        self.assertIs(company["follow_on"], True)

    def test_refuses_to_build_when_the_check_fails(self):
        with tempfile.TemporaryDirectory() as d:
            make_data(d, [ALPHA.replace("site/logos/alpha.svg", "site/logos/missing.svg")])
            (Path(d) / "site/logos/missing.svg").unlink()
            with self.assertRaises(SystemExit):
                build(d, d)


if __name__ == "__main__":
    unittest.main()
