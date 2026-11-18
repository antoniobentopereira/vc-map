# One value per field; conflicting Sources are weighed, not kept side by side

Amends ADR 0002, which said several Sources for one fact are several rows.

The site shows one value per field, so the Dataset holds one. When Sources disagree (Tractian's pre-seed is R$2M in the press and US$500k in an aggregator), the researcher weighs them, keeps the most likely value with its Source and Confidence, and writes the discarded values and the reasoning in the note. The check script rejects a second row for a single-value field. List fields (founders, markets, accelerators, milestones) still take one row per value.

Because a field with no row is ambiguous between "not found" and "not researched", `companies.csv` records `researched_on`: once it is set, a missing field means the information was not publicly available on that date. Fields that change over time (status, HQ, the latest Round) are read as of that date.
