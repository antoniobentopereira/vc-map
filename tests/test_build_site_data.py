import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from build_site_data import build, slugify  # noqa: E402
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

    def test_slugs_are_ascii_and_unique(self):
        self.assertEqual(slugify("NG.CASH"), "ng-cash")
        self.assertEqual(slugify("Açaí & Café!"), "acai-cafe")
        twin = BETA.replace("Beta Co.", "beta co").replace("beta.png", "beta2.png")
        slugs = [c["slug"] for c in self.build([BETA, twin])["companies"]]
        self.assertEqual(slugs, ["beta-co", "beta-co-2"])

    def test_refuses_to_build_when_the_check_fails(self):
        with tempfile.TemporaryDirectory() as d:
            make_data(d, [ALPHA.replace("site/logos/alpha.svg", "site/logos/missing.svg")])
            (Path(d) / "site/logos/missing.svg").unlink()
            with self.assertRaises(SystemExit):
                build(d, d)

    def test_output_is_json_serialisable(self):
        json.dumps(self.build([ALPHA]))


if __name__ == "__main__":
    unittest.main()
