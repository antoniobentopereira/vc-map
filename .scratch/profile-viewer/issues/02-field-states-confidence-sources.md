# 02: Field states, confidence and sources

**What to build:** Every field in the Facts box shows its state. Reported values are plain; uncertain ones (Basis `estimated` or Confidence `low`) get a dashed amber border, an "EST" or "LOW" tag and a visible note; a field with no row shows a red "NOT FOUND (as of the `researched_on` date)" placeholder when researched, or a red-outlined "NOT RESEARCHED" placeholder when `researched_on` is empty, with a banner on the profile. Acquirer and acquisition year read "none recorded (not acquired, or not found)". Every value has a confidence dot (green high, yellow medium, red low), a Basis tag, its note when present, and a small "source" button that reveals the link with Open (new tab) and Copy. The header carries a legend for the dots and tags. Medium counts as certain enough.

**Blocked by:** 01 (Tracer bullet: generate data and open a company profile).

**Status:** resolved

- [x] All four states are visibly distinct and match the spec's wording
- [x] Confidence dot, Basis, note and "source" button (Open, Copy) appear on every value that has them
- [x] No raw URLs in the page body
- [x] Checked by hand on a fully researched company and on a thin or unresearched one
