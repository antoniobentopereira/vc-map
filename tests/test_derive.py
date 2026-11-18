import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from derive import first_investment, follow_on, last_round  # noqa: E402


def round_row(year, round_type, norte=False):
    return {"year": str(year), "type": round_type, "norte_participated": "TRUE" if norte else "FALSE"}


class FirstInvestmentTest(unittest.TestCase):
    def test_earliest_round_norte_took_part_in(self):
        rounds = [round_row(2023, "series_b", True), round_row(2021, "seed", True), round_row(2020, "angel"), round_row(2021, "pre_seed", True)]
        self.assertEqual(first_investment(rounds), round_row(2021, "pre_seed", True))

    def test_none_when_no_recorded_round_has_norte(self):
        self.assertIsNone(first_investment([round_row(2021, "seed")]))


class LastRoundTest(unittest.TestCase):
    def test_latest_equity_round_whether_or_not_norte_took_part(self):
        rounds = [round_row(2021, "pre_seed", True), round_row(2026, "series_d"), round_row(2024, "series_c", True)]
        self.assertEqual(last_round(rounds), round_row(2026, "series_d"))

    def test_debt_never_counts(self):
        rounds = [round_row(2024, "series_c"), round_row(2025, "debt")]
        self.assertEqual(last_round(rounds), round_row(2024, "series_c"))
        self.assertIsNone(last_round([round_row(2025, "debt")]))

    def test_later_stage_wins_within_the_same_year(self):
        self.assertEqual(last_round([round_row(2022, "series_a"), round_row(2022, "seed")]), round_row(2022, "series_a"))

    def test_a_round_of_unknown_type_never_beats_a_known_stage_in_the_same_year(self):
        rounds = [round_row(2022, "series_a"), round_row(2022, "unknown")]
        self.assertEqual(last_round(rounds), round_row(2022, "series_a"))
        self.assertEqual(last_round([round_row(2021, "seed"), round_row(2022, "unknown")]), round_row(2022, "unknown"))

    def test_can_be_the_first_investment(self):
        rounds = [round_row(2025, "seed", True)]
        self.assertEqual(last_round(rounds), first_investment(rounds))


class FollowOnTest(unittest.TestCase):
    def test_true_when_norte_took_part_in_a_later_round(self):
        self.assertIs(follow_on([round_row(2021, "pre_seed", True), round_row(2021, "seed", True)]), True)

    def test_false_when_norte_took_part_once(self):
        self.assertIs(follow_on([round_row(2021, "pre_seed", True), round_row(2023, "series_b")]), False)

    def test_unknown_when_no_recorded_round_has_norte(self):
        self.assertIsNone(follow_on([round_row(2023, "series_b")]))


if __name__ == "__main__":
    unittest.main()
