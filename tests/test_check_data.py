import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_data import (
    ALLOWED_LOGO_BACKGROUNDS,  # noqa: E402
    ALLOWED_BUSINESS_MODELS,
    ALLOWED_FIELDS,
    ALLOWED_NORTE,
    ALLOWED_STATUS,
    ROUND_TYPES,
    check_files,
    follow_up_companies,
)

ROOT = Path(__file__).resolve().parent.parent
HEADER = "name,website,fund,is_highlight,is_exit,logo,logo_background,logo_origin,logo_source,researched_on"
ALPHA = "Alpha,https://alpha.com,I,FALSE,FALSE,site/logos/alpha.svg,,company-site,https://alpha.com/logo.svg,"
HEADERS = {
    "claims": "company,field,value,source_url,basis,confidence,note",
    "rounds": "company,year,type,reported_amount,reported_currency,size_usd,co_investors,"
              "norte_participated,source_url,basis,confidence,note",
    "fx": "currency,year,rate,source_url",
    "sectors": "sub_sector,sector",
}


def write(directory, name, lines):
    path = Path(directory) / name
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def touch_logos(root, lines):
    for line in lines[1:]:
        logo = line.split(",")[5]
        if logo:
            (Path(root) / logo).parent.mkdir(parents=True, exist_ok=True)
            (Path(root) / logo).write_bytes(b"x")


def run(companies=(ALPHA,), raw=None, **tables):
    """Write a data folder (companies plus any of claims/rounds/fx/sectors) and check it.

    Table lines get their header added; `raw` maps file names to full contents (header included)."""
    with tempfile.TemporaryDirectory() as d:
        company_lines = [HEADER, *companies]
        touch_logos(d, company_lines)
        write(d, "companies.csv", company_lines)
        for name, lines in tables.items():
            write(d, f"{name}.csv", [HEADERS[name], *lines])
        for name, lines in (raw or {}).items():
            write(d, name, lines)
        return check_files(d, d)


class Assertions(unittest.TestCase):
    def assertOneError(self, errors, fragment, line=None):
        self.assertEqual(len(errors), 1, errors)
        self.assertIn(fragment, errors[0])
        if line:
            self.assertIn(f"line {line}", errors[0])


class CompaniesTest(Assertions):
    def check(self, *lines):
        return run(companies=lines)

    def test_real_shape_passes(self):
        self.assertEqual(self.check(ALPHA), [])

    def test_logo_background_values(self):
        for value in ("dark", "light", "both", ""):
            self.assertEqual(self.check(ALPHA.replace(".svg,,company-site", f".svg,{value},company-site")), [])
        self.assertOneError(self.check(ALPHA.replace(".svg,,company-site", ".svg,grey,company-site")), "logo_background 'grey'")

    def test_logo_background_without_logo_is_an_error(self):
        self.assertOneError(self.check("Alpha,https://a.com,I,FALSE,FALSE,,dark,,,"), "logo is empty")

    def test_missing_logo_file(self):
        with tempfile.TemporaryDirectory() as d:
            write(d, "companies.csv", [HEADER, ALPHA])
            errors = check_files(d, d)
        self.assertOneError(errors, "logo file 'site/logos/alpha.svg' does not exist")

    def test_empty_logo_is_valid_and_listed_for_follow_up(self):
        self.assertEqual(self.check("Alpha,https://a.com,I,FALSE,FALSE,,,,,"), [])
        self.assertEqual(follow_up_companies([{"name": "Alpha", "logo": ""}, {"name": "B", "logo": "x"}]), ["Alpha"])

    def test_set_logo_needs_valid_origin(self):
        self.assertOneError(self.check("Alpha,https://a.com,I,FALSE,FALSE,site/logos/a.svg,,,https://a.com/l.svg,"), "logo_origin")
        self.assertOneError(self.check("Alpha,https://a.com,I,FALSE,FALSE,site/logos/a.svg,,norte,https://a.com/l.svg,"), "logo_origin 'norte'")

    def test_set_logo_needs_valid_source_url(self):
        self.assertOneError(self.check("Alpha,https://a.com,I,FALSE,FALSE,site/logos/a.svg,,manual,,"), "logo_source")
        self.assertOneError(self.check("Alpha,https://a.com,I,FALSE,FALSE,site/logos/a.svg,,manual,not a url,"), "logo_source")

    def test_norte_source_is_an_error(self):
        self.assertOneError(
            self.check("Alpha,https://a.com,I,FALSE,FALSE,site/logos/a.svg,,manual,https://www.norte.ventures/x.svg,"),
            "norte.ventures",
        )

    def test_documented_norte_exception_is_allowed_only_for_listed_companies(self):
        line = "{},https://a.com,I,FALSE,FALSE,site/logos/a.svg,,manual,https://www.norte.ventures/x.svg,"
        self.assertEqual(self.check(line.format("Glue")), [])
        self.assertOneError(self.check(line.format("Other")), "norte.ventures")

    def test_empty_logo_with_leftover_origin_or_source_is_an_error(self):
        self.assertOneError(self.check("Alpha,https://a.com,I,FALSE,FALSE,,,manual,,"), "logo is empty")
        self.assertOneError(self.check("Alpha,https://a.com,I,FALSE,FALSE,,,,https://a.com/l.svg,"), "logo is empty")

    def test_duplicate_company(self):
        errors = self.check(ALPHA, "alpha,https://b.com,II,FALSE,FALSE,site/logos/alpha.svg,,manual,https://a.com/p,")
        self.assertOneError(errors, "duplicate of line 2")

    def test_invalid_website(self):
        self.assertOneError(self.check("Alpha,alpha,I,FALSE,FALSE,site/logos/alpha.svg,,manual,https://a.com/p,"), "website")

    def test_bad_fund_and_flag(self):
        errors = self.check("Alpha,https://a.com,III,yes,FALSE,site/logos/alpha.svg,,manual,https://a.com/p,")
        self.assertEqual(len(errors), 2, errors)

    def test_researched_on_is_empty_or_a_past_date(self):
        base = "Alpha,https://a.com,I,FALSE,FALSE,,,,,{}"
        self.assertEqual(self.check(base.format("2026-11-18")), [])
        self.assertOneError(self.check(base.format("18/11/2026")), "researched_on '18/11/2026'")
        self.assertOneError(self.check(base.format("2026-02-30")), "researched_on '2026-02-30'")
        self.assertOneError(self.check(base.format("2999-01-01")), "is in the future")

    def test_wrong_columns(self):
        with tempfile.TemporaryDirectory() as d:
            write(d, "companies.csv", ["name,website", "Alpha,https://a.com"])
            errors = check_files(d, d)
        self.assertOneError(errors, "columns must be exactly")


GOOD = "Alpha,description,Payments app for shops.,https://alpha.com/about,reported,high,"


class ClaimsTest(Assertions):
    def test_correct_sample_passes(self):
        self.assertEqual(run(claims=[GOOD, "Alpha,founder,Ana Lima,https://x.com/a,estimated,low,Named in a podcast"]), [])

    def one(self, line, fragment):
        self.assertOneError(run(claims=[line]), fragment, line=2)

    def test_missing_source_link(self):
        self.one("Alpha,description,Shop app.,,reported,high,", "source_url is empty")

    def test_invalid_url(self):
        self.one("Alpha,description,Shop app.,not a url,reported,high,", "not a valid URL")
        self.one("Alpha,description,Shop app.,ftp://a.com/x,reported,high,", "not a valid URL")

    def test_unknown_company(self):
        self.one("Ghost,description,Shop app.,https://a.com,reported,high,", "unknown company 'Ghost'")

    def test_unknown_or_retired_field(self):
        self.one("Alpha,colour,Blue,https://a.com,reported,high,", "field 'colour' is not allowed")
        self.one("Alpha,round_size,1000,https://a.com,reported,high,", "field 'round_size' is not allowed")
        self.one("Alpha,sector,Fintech,https://a.com,reported,high,", "field 'sector' is not allowed")

    def test_bad_basis_and_confidence(self):
        self.one("Alpha,description,Shop app.,https://a.com,guess,high,", "basis 'guess'")
        self.one("Alpha,description,Shop app.,https://a.com,reported,sure,", "confidence 'sure'")

    def test_estimated_needs_note(self):
        self.one("Alpha,description,Shop app.,https://a.com,estimated,low,", "estimated claim needs a note")

    def test_empty_value(self):
        self.one("Alpha,description,,https://a.com,reported,high,", "value is empty")

    def test_line_numbers_stay_right_after_blank_and_multi_line_rows(self):
        errors = run(raw={"claims.csv": [
            HEADERS["claims"], 'Alpha,long_description,"Two\nlines",https://a.com,reported,high,', "",
            "Alpha,founder,,https://a.com,reported,high,",
        ]})
        self.assertEqual(len(errors), 2, errors)
        self.assertIn("line 2", errors[0])
        self.assertIn("claims.csv line 5: value is empty", errors[1])

    def test_value_on_several_lines(self):
        self.one('Alpha,long_description,"First line.\nSecond line.",https://a.com,reported,high,', "line break")

    def test_exact_duplicate(self):
        errors = run(claims=[GOOD.replace("description", "founder"), GOOD.replace("description", "founder")])
        self.assertOneError(errors, "duplicate of line 2", line=3)

    def test_list_fields_take_one_row_per_value(self):
        rows = [f"Alpha,{field},{value},https://a.com,reported,high," for field, value in [
            ("founder", "Ana"), ("founder", "Bo"), ("market", "Brazil"), ("market", "Mexico"),
            ("accelerator", "Y Combinator"), ("accelerator", "Endeavor"),
        ]]
        self.assertEqual(run(claims=rows), [])

    def test_single_value_fields_take_one_row(self):
        errors = run(claims=[GOOD, "Alpha,description,Another text.,https://b.com,reported,low,"])
        self.assertOneError(errors, "second 'description' for Alpha", line=3)
        self.assertIn("weigh the sources", errors[0])

    def test_investment_thesis_is_a_single_value_field(self):
        thesis = 'Alpha,investment_thesis,"Why it works.",https://a.com,estimated,medium,Reasoned from the market size.'
        self.assertEqual(run(claims=[GOOD, thesis]), [])
        errors = run(claims=[GOOD, thesis, thesis.replace("Why it works.", "Another view.")])
        self.assertOneError(errors, "second 'investment_thesis' for Alpha", line=4)


def claim(field, value):
    return f'Alpha,{field},"{value}",https://a.com,reported,high,'


class ClaimValueTest(Assertions):
    def valid(self, field, *values):
        for value in values:
            self.assertEqual(run(claims=[claim(field, value)]), [], (field, value))

    def invalid(self, field, value, fragment):
        self.assertOneError(run(claims=[claim(field, value)]), fragment, line=2)

    def test_years(self):
        for field in ("year_founded", "acquisition_year"):
            self.valid(field, "2019")
            self.invalid(field, "19", "must be a year")
            self.invalid(field, "2019 (approx.)", "must be a year")
            self.invalid(field, "1850", "must be a year")
            self.invalid(field, "2999", "must be a year")

    def test_status(self):
        self.valid("status", "stealth", "active", "inactive", "closed")
        self.invalid("status", "acquired", "status 'acquired' must be one of stealth, active, inactive, closed")
        self.invalid("status", "Active", "status 'Active'")

    def test_business_model(self):
        self.valid("business_model", "b2b", "b2c", "b2b2c")
        self.invalid("business_model", "B2B", "business_model 'B2B'")

    def test_hq_is_city_comma_country(self):
        for field in ("hq", "hq_at_first_investment"):
            self.valid(field, "São Paulo, Brazil", "Mexico City, Mexico")
            self.invalid(field, "São Paulo", "must look like 'City, Country'")
            self.invalid(field, "São Paulo,Brazil", "must look like 'City, Country'")
            self.invalid(field, "Atlanta, GA, United States", "must look like 'City, Country'")

    def test_milestone_starts_with_a_date(self):
        self.valid("milestone", "2021: Joined Y Combinator", "2021-03: Joined Y Combinator", "2021-03-19: Demo Day")
        self.invalid("milestone", "Joined Y Combinator in 2021", "must start with a date")
        self.invalid("milestone", "2021 Joined Y Combinator", "must start with a date")
        self.invalid("milestone", "2021-13: Joined Y Combinator", "must start with a date")
        self.invalid("milestone", "2021:", "must start with a date")

    def test_acquisition_not_before_founding(self):
        errors = run(claims=[claim("year_founded", "2019"), claim("acquisition_year", "2018")])
        self.assertOneError(errors, "acquisition_year 2018 is before year_founded 2019")


class SectorsTest(Assertions):
    def test_sub_sector_listed_with_or_without_a_sector_passes(self):
        sectors = ["Industrial AI,", "Payments,Fintech"]
        self.assertEqual(run(claims=[claim("sub_sector", "Industrial AI")], sectors=sectors), [])

    def test_sub_sector_missing_from_sectors_file(self):
        errors = run(claims=[claim("sub_sector", "Industrial AI")], sectors=["Payments,Fintech"])
        self.assertOneError(errors, "sub_sector 'Industrial AI' is not in sectors.csv", line=2)

    def test_sub_sector_needs_a_sectors_file(self):
        self.assertOneError(run(claims=[claim("sub_sector", "Industrial AI")]), "is not in sectors.csv")

    def test_sectors_file_rows(self):
        self.assertOneError(run(sectors=[",Fintech"]), "sectors.csv line 2: sub_sector is empty")
        self.assertOneError(run(sectors=["Payments,Fintech", "payments,"]), "sectors.csv line 3: duplicate of line 2")


FX = "BRL,2021,5.3956,https://api.bcb.gov.br/dados/serie/bcdata.sgs.3694/dados?formato=json"


class FxTest(Assertions):
    def test_good_rate_passes(self):
        self.assertEqual(run(fx=[FX, FX.replace("BRL,2021", "MXN,2021")]), [])

    def one(self, line, fragment):
        self.assertOneError(run(fx=[line]), fragment, line=2)

    def test_currency_is_a_three_letter_code_other_than_usd(self):
        self.one(FX.replace("BRL", "R$"), "currency 'R$'")
        self.one(FX.replace("BRL", "brl"), "currency 'brl'")
        self.one(FX.replace("BRL", "USD"), "currency 'USD'")

    def test_year_rate_and_source(self):
        self.one(FX.replace("2021", "21", 1), "year '21'")
        self.one(FX.replace("5.3956", '"5,39"'), "rate '5,39'")
        self.one(FX.replace("5.3956", "0"), "rate '0'")
        self.one(FX.replace("https://api", "api"), "source_url")

    def test_one_rate_per_currency_and_year(self):
        errors = run(fx=[FX, FX.replace("5.3956", "5.40")])
        self.assertOneError(errors, "duplicate of line 2", line=3)


# R$ 2,000,000 at 5.3956 BRL per USD is US$ 370,672 (5.3956 x 370,672 = 1,999,997.8).
ROUND = "Alpha,2021,pre_seed,2000000,BRL,370672,Y Combinator; Soma Capital,TRUE,https://a.com/news,reported,high,"


def round_line(**changes):
    """ROUND with some columns replaced, e.g. round_line(type="seed")."""
    columns = HEADERS["rounds"].split(",")
    values = ROUND.split(",")
    for name, value in changes.items():
        values[columns.index(name)] = value
    return ",".join(values)


class RoundsTest(Assertions):
    def check(self, *rounds, claims=()):
        return run(rounds=rounds, fx=[FX], claims=list(claims))

    def one(self, line, fragment):
        self.assertOneError(self.check(line), fragment, line=2)

    def test_converted_round_passes(self):
        self.assertEqual(self.check(ROUND), [])

    def test_usd_round_needs_no_rate(self):
        self.assertEqual(self.check(round_line(reported_amount="3200000", reported_currency="USD", size_usd="3200000")), [])

    def test_undisclosed_size_leaves_all_three_amount_columns_empty(self):
        self.assertEqual(self.check(round_line(reported_amount="", reported_currency="", size_usd="")), [])
        self.one(round_line(reported_currency="", size_usd=""), "fill reported_amount and reported_currency together")
        self.one(round_line(reported_amount="", reported_currency=""), "size_usd needs reported_amount and reported_currency")

    def test_amounts_are_whole_numbers(self):
        self.one(round_line(reported_amount="2M"), "reported_amount '2M' must be a whole number")
        self.one(round_line(size_usd="370672.4"), "size_usd '370672.4' must be a whole number")

    def test_size_usd_must_match_the_fx_rate(self):
        self.one(round_line(size_usd="371000"), "size_usd 371000 does not match 2000000 BRL at 5.3956 (expected 370672)")
        self.one(round_line(reported_currency="USD"), "size_usd 370672 does not match 2000000 USD (expected 2000000)")

    def test_converted_round_needs_a_rate_for_its_currency_and_year(self):
        self.one(round_line(year="2022"), "no BRL rate for 2022 in fx.csv")
        self.one(round_line(reported_currency="MXN"), "no MXN rate for 2021 in fx.csv")

    def test_type_year_and_norte_flag(self):
        for good in ("angel", "seed", "series_a", "series_f_plus", "debt", "unknown"):
            self.assertEqual(self.check(round_line(type=good)), [], good)
        self.one(round_line(type="Series A"), "type 'Series A' must be one of angel, pre_seed")
        self.one(round_line(type="bridge"), "type 'bridge'")
        self.one(round_line(year="21"), "year '21'")
        self.one(round_line(norte_participated="yes"), "norte_participated 'yes' must be TRUE, FALSE or UNKNOWN")

    def test_norte_participation_can_be_unknown(self):
        for flag in ("TRUE", "FALSE", "UNKNOWN"):
            self.assertEqual(self.check(round_line(norte_participated=flag)), [], flag)

    def test_company_source_basis_confidence(self):
        self.one(round_line(company="Ghost"), "unknown company 'Ghost'")
        self.one(round_line(source_url=""), "source_url is empty")
        self.one(round_line(source_url="news"), "not a valid URL")
        self.one(round_line(basis="guess"), "basis 'guess'")
        self.one(round_line(basis="estimated"), "estimated round needs a note")
        self.one(round_line(confidence="sure"), "confidence 'sure'")

    def test_co_investors_on_one_line(self):
        self.one(round_line(co_investors='"Y Combinator;\nSoma"'), "co_investors has a line break")

    def test_duplicate_round(self):
        self.assertOneError(self.check(ROUND, ROUND), "duplicate of line 2", line=3)

    def test_one_row_per_round_even_when_sources_disagree_on_the_amount(self):
        errors = self.check(ROUND, round_line(reported_amount="", reported_currency="", size_usd=""))
        self.assertOneError(errors, "second pre_seed in 2021 for Alpha", line=3)
        self.assertIn("discarded", errors[0])

    def test_amount_can_wait_for_a_rate_not_yet_published(self):
        pending = round_line(year="2026", size_usd="")
        self.assertEqual(self.check(pending), [])
        self.one(round_line(size_usd=""), "compute size_usd from the 2021 BRL rate in fx.csv")

    def test_round_not_before_founding(self):
        errors = self.check(round_line(year="2018", reported_amount="", reported_currency="", size_usd=""),
                            claims=[claim("year_founded", "2019")])
        self.assertOneError(errors, "round year 2018 is before year_founded 2019")


def undocumented(terms, doc_text):
    """The terms that docs/data-model.md does not mention (as a whole word)."""
    return [t for t in terms if not re.search(rf"(?<![\w]){re.escape(t)}(?![\w])", doc_text)]


class DocsMatchCodeTest(unittest.TestCase):
    """docs/data-model.md is the field reference; the allowed values in the script must all appear in it."""

    def test_every_allowed_value_is_documented(self):
        doc = (ROOT / "docs" / "data-model.md").read_text(encoding="utf-8")
        for name, terms in {
            "claim fields": ALLOWED_FIELDS,
            "round types": ROUND_TYPES,
            "status values": ALLOWED_STATUS,
            "logo backgrounds": ALLOWED_LOGO_BACKGROUNDS,
            "business models": ALLOWED_BUSINESS_MODELS,
            "Norte participation values": ALLOWED_NORTE,
        }.items():
            self.assertEqual(undocumented(terms, doc), [], f"{name} missing from docs/data-model.md")

    def test_a_missing_term_is_reported(self):
        self.assertEqual(undocumented(["hq", "seed", "series_f_plus"], "`hq` and `seed`"), ["series_f_plus"])


class RealDataTest(unittest.TestCase):
    def test_real_data_passes(self):
        self.assertEqual(check_files(), [])


if __name__ == "__main__":
    unittest.main()
