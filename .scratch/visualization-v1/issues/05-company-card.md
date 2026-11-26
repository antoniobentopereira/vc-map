# 05: Company card

Spec: `.scratch/visualization-v1/spec.md`

**What to build:** Clicking or tapping a Logo dot stops it and opens a small, centered Company card with the company's essentials, where Estimated values look visibly different. Closing the card lets the dot drift again.

**Blocked by:** 02

**Status:** ready-for-agent

- [ ] The site data builder carries `{value, basis, confidence, source}` for the card's fields, plus each company's Sector from the mapping (absent while the mapping is empty). Tested at the builder seam.
- [ ] Clicking or tapping a dot pauses only that dot and opens the card: name, logo, Sector, short description, year founded and Fund.
- [ ] Estimated values use the convention: muted brown, dotted underline, "≈" before numbers. Hover or tap shows the Basis, Confidence and Source.
- [ ] A missing value reads "not publicly available".
- [ ] The card closes by clicking outside it, with a close button or with Escape, and the dot then resumes drifting.
- [ ] An "Open full card" button is present. It leads to the profile once ticket 06 lands.
- [ ] Works by tap at 320px. Checked in the browser.
