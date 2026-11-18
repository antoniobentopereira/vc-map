# Stages and definitions of done

Data first, visualization second. The CSV files in `data/` are the single source of truth, edited by hand in VS Code. Research is done one company at a time until the process is proven; sub-agents are an idea for later scale-up.

## 1. Roster
`companies` lists every unique Portfolio company (about 130) with name, website, logo file, Fund (I or II), `is_highlight` and `is_exit`. The count matches the official page, duplicates are reported, and the owner has looked through it.

## 2. Pilot (Batch 1, 10 companies, one at a time)
All Batch 1 fields are filled: description, sector, location, year founded, investment year, status, round size, co-investors, founder names. Every Claim has a source link, a Basis and a Confidence. The check script passes (required source links, valid URLs, allowed field values, no duplicates), and the owner has reviewed all 10 and given feedback that is folded back into the process.

## 3. Scale-up
Remaining companies are researched in Batches (bigger once the Pilot works). Each Batch passes the check script and the owner spot-checks a sample. Done when every company in the Roster is covered. The owner may add new fields along the way.

## 4. Visualization v1 (starts after a couple of Batches)
Definition of done is set when this stage starts, since the owner expects the data work to shape it. Fixed constraints: static `site/` folder, works at 320px by tap, unofficial notice, visibly different colour for Estimated Claims, works when copied into `mysite/public/vc-map/`.

## Later, out of v1
Deep Founder profiles (education, past roles, other companies): own plan and own ADR.
