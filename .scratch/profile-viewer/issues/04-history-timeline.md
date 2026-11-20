# 04: History timeline

**What to build:** A visual, year-anchored timeline merging Milestones (from Claims) and Rounds (from `rounds.csv`) chronologically. Rounds are styled differently from Milestones. Partial dates (`2021`, `2021-03`, `2021-03-19`) sort with month- or day-dated items before year-only items within a year; Rounds have a year only. A company with no Milestones or Rounds shows the "not found" or "not researched" placeholder.

**Blocked by:** 02 (Field states, confidence and sources).

**Status:** resolved

- [x] Timeline reads clearly as history, with years as anchors
- [x] Rounds and Milestones are visually distinct
- [x] Sort order follows the rule for partial dates
- [x] Empty history shows the correct placeholder
