# Stages and definitions of done

Data first, visualization second. The CSV files in `data/` are the single source of truth, edited by hand in VS Code. Research is done one company at a time until the process is proven; sub-agents are an idea for later scale-up.

## 1. Roster
`companies` lists every unique Portfolio company (about 130) with name, website, logo file, Fund (I or II), `is_highlight` and `is_exit`. The count matches the official page, duplicates are reported, and the owner has looked through it.

## 2. Pilot (Batch 1, 10 companies, one at a time)
Every field in `docs/data-model.md` is filled or recorded as missing: the Claims (description, long description, sub-sector, HQ now and at the first investment, year founded, status, business model, acquisition, founders, markets, accelerators, milestones) and every Round found, with or without Norte. Every Claim and Round has a source link, a Basis and a Confidence, and the company's `researched_on` date is set. The check script passes (required source links, valid URLs, allowed field values and formats, one value per field, USD sizes matching `fx.csv`, no duplicates), and the owner has reviewed all 10 and given feedback that is folded back into the process.

## 3. Scale-up
Remaining companies are researched in Batches (bigger once the Pilot works). Each Batch passes the check script and the owner spot-checks a sample. Done when every company in the Roster is covered. The owner may add new fields along the way.

## 4. Visualization v1 (starts after a couple of Batches)
Definition of done is set when this stage starts, since the owner expects the data work to shape it. Fixed constraints: static `site/` folder, works at 320px by tap, unofficial notice, visibly different colour for Estimated Claims, works when copied into `mysite/public/vc-map/`.

## Later, out of v1
Deep Founder profiles (education, past roles, other companies): own plan and own ADR.
