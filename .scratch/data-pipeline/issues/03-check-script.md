# 03: Check script: validate the data files

**What to build:** A Python script that fixes the columns of the claims CSV (company, field, value, source_url, basis, confidence, note) and the allowed values for `field`, `basis` (reported/estimated) and `confidence` (high/medium/low). It checks completeness and data types only: every Claim has a source link, every URL is valid, every Claim points at a real company in the companies CSV, estimated Claims have a note, and there are no duplicates. It prints readable errors. It is tested on a tiny sample file with deliberate mistakes, and passes on the real companies CSV.

**Blocked by:** 01 (Roster).

**Status:** resolved

- [ ] Each rule above is caught by a deliberate-mistake sample, with a clear message
- [ ] A correct sample passes
- [ ] The real companies CSV passes (no duplicates, valid website URLs)
- [ ] The allowed field list comes from the Batch 1 fields in the stages doc
