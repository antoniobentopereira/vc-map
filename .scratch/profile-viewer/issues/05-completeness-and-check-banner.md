# 05: Completeness indicator and check-errors banner

**What to build:** The header shows completeness such as "11 / 13 filled, 2 uncertain, 2 not found", or "not researched" when `researched_on` is empty. It counts the single-value fields (the two acquisition fields excluded), the four list fields and Rounds, with exact denominators taken from `docs/data-model.md`; uncertain values count as filled and are also counted separately. A banner shows any findings from the existing data check (`check_files`) for the selected company.

**Blocked by:** 03 (Founders, markets, accelerators and Rounds).

**Status:** resolved

- [x] Completeness numbers match what is visibly on the profile for a real company
- [x] Acquisition fields are not counted
- [x] The check banner reuses the existing check, not a copy of its rules
