# 03: Founders, markets, accelerators and Rounds

**What to build:** The right column. Founders, markets and accelerators show as stacks of small boxes, each row carrying the same state, dot, Basis, note and source button as in ticket 02, and a placeholder when empty. The Investment Rounds table shows type, year, size in USD and whether Norte took part, with a second line per Round for the reported amount, currency and co-investors. A summary line above it shows the first investment, last round and follow-on, computed with the existing `derive.py` logic (not reimplemented). A flag shows when no Norte Round is recorded; a company with no Rounds shows the missing placeholder.

**Blocked by:** 02 (Field states, confidence and sources).

**Status:** resolved

- [x] List fields and Rounds render with per-row sources and states
- [x] First investment, last round and follow-on come from `derive.py`
- [x] "No Norte round recorded" flag appears when applicable
- [x] Empty lists and no Rounds show the right red placeholder
