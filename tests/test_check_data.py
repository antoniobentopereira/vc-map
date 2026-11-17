import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_data import (  # noqa: E402
    ALLOWED_FIELDS,
    check_claims,
    check_companies,
    check_files,
)

ROOT = Path(__file__).resolve().parent.parent
COMPANIES = ["name,website,fund,is_highlight,is_exit", "Alpha,https://alpha.com,I,FALSE,FALSE"]
CLAIMS_HEADER = "company,field,value,source_url,basis,confidence,note"


def write(directory, name, lines):
    path = Path(directory) / name
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def run(claim_lines, company_lines=COMPANIES):
    with tempfile.TemporaryDirectory() as d:
        companies = write(d, "companies.csv", company_lines)
        claims = write(d, "claims.csv", [CLAIMS_HEADER, *claim_lines])
        return check_files(companies, claims)


GOOD = "Alpha,sector,Fintech,https://alpha.com/about,reported,high,"


class ClaimsTest(unittest.TestCase):
    def test_correct_sample_passes(self):
        self.assertEqual(run([GOOD, "Alpha,round_size,~1M,https://x.com/a,estimated,low,Inferred from press"]), [])

    def assertOneError(self, line, fragment):
        errors = run([line])
        self.assertEqual(len(errors), 1, errors)
        self.assertIn(fragment, errors[0])
        self.assertIn("line 2", errors[0])

    def test_missing_source_link(self):
        self.assertOneError("Alpha,sector,Fintech,,reported,high,", "source_url is empty")

    def test_invalid_url(self):
        self.assertOneError("Alpha,sector,Fintech,not a url,reported,high,", "not a valid URL")

    def test_non_http_url(self):
        self.assertOneError("Alpha,sector,Fintech,ftp://a.com/x,reported,high,", "not a valid URL")

    def test_unknown_company(self):
        self.assertOneError("Ghost,sector,Fintech,https://a.com,reported,high,", "unknown company 'Ghost'")

    def test_unknown_field(self):
        self.assertOneError("Alpha,colour,Blue,https://a.com,reported,high,", "field 'colour' is not allowed")

    def test_bad_basis(self):
        self.assertOneError("Alpha,sector,Fintech,https://a.com,guess,high,", "basis 'guess'")

    def test_bad_confidence(self):
        self.assertOneError("Alpha,sector,Fintech,https://a.com,reported,sure,", "confidence 'sure'")

    def test_estimated_needs_note(self):
        self.assertOneError("Alpha,sector,Fintech,https://a.com,estimated,low,", "estimated claim needs a note")

    def test_empty_value(self):
        self.assertOneError("Alpha,sector,,https://a.com,reported,high,", "value is empty")

    def test_duplicate(self):
        errors = run([GOOD, GOOD])
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("duplicate of line 2", errors[0])
        self.assertIn("line 3", errors[0])

    def test_same_field_different_value_is_not_duplicate(self):
        other = "Alpha,co_investors,Fund B,https://a.com,reported,high,"
        third = "Alpha,co_investors,Fund C,https://a.com,reported,high,"
        self.assertEqual(run([other, third]), [])

    def test_wrong_columns(self):
        with tempfile.TemporaryDirectory() as d:
            companies = write(d, "companies.csv", COMPANIES)
            claims = write(d, "claims.csv", ["company,field,value", "Alpha,sector,Fintech"])
            errors = check_files(companies, claims)
        self.assertEqual(len(errors), 1)
        self.assertIn("columns must be exactly", errors[0])

    def test_missing_claims_file_is_fine(self):
        with tempfile.TemporaryDirectory() as d:
            companies = write(d, "companies.csv", COMPANIES)
            self.assertEqual(check_files(companies, Path(d) / "claims.csv"), [])


class CompaniesTest(unittest.TestCase):
    def check(self, *lines):
        with tempfile.TemporaryDirectory() as d:
            path = write(d, "companies.csv", ["name,website,fund,is_highlight,is_exit", *lines])
            return check_files(path, Path(d) / "none.csv")

    def test_duplicate_company(self):
        errors = self.check("Alpha,https://a.com,I,FALSE,FALSE", "alpha,https://b.com,II,FALSE,FALSE")
        self.assertEqual(len(errors), 1)
        self.assertIn("duplicate of line 2", errors[0])

    def test_invalid_website(self):
        errors = self.check("Alpha,alpha,I,FALSE,FALSE")
        self.assertEqual(len(errors), 1)
        self.assertIn("website", errors[0])

    def test_bad_fund_and_flag(self):
        errors = self.check("Alpha,https://a.com,III,yes,FALSE")
        self.assertEqual(len(errors), 2, errors)


class FieldListTest(unittest.TestCase):
    def test_fields_match_batch_1_in_stages_doc(self):
        self.assertEqual(
            set(ALLOWED_FIELDS),
            {
                "description", "sector", "location", "year_founded", "investment_year",
                "status", "round_size", "co_investors", "founder_names",
            },
        )


class RealDataTest(unittest.TestCase):
    def test_real_companies_csv_passes(self):
        self.assertEqual(check_files(ROOT / "data" / "companies.csv", ROOT / "data" / "claims.csv"), [])


if __name__ == "__main__":
    unittest.main()
