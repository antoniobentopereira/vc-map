"""Views derived from one company's rows in data/rounds.csv (see docs/data-model.md).

An Investment is a Round the Firm (Norte) took part in. Rounds are ordered by year, then by stage within
the same year; a Round of unknown type has no stage, so within its year it comes before every known one.
"""
from check_data import ROUND_TYPES

STAGES = [t for t in ROUND_TYPES if t not in ("unknown", "debt")]


def _order(round_):
    stage = STAGES.index(round_["type"]) if round_["type"] in STAGES else -1
    return int(round_["year"]), stage


def _investments(rounds):
    return sorted((r for r in rounds if r["norte_participated"] == "TRUE"), key=_order)


def first_investment(rounds):
    """The earliest Round Norte took part in, or None if no recorded Round has Norte."""
    investments = _investments(rounds)
    return investments[0] if investments else None


def last_round(rounds):
    """The latest equity Round, whether or not Norte took part. Debt never counts."""
    equity = [r for r in rounds if r["type"] != "debt"]
    return max(equity, key=_order) if equity else None


def follow_on(rounds):
    """True if Norte took part in more than one Round, False if in one, None if in none recorded."""
    investments = _investments(rounds)
    return len(investments) > 1 if investments else None
