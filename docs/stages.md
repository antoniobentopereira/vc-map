# Stages and definitions of done

Data first, visualization second. The CSV files in `data/` are the single source of truth, edited by hand in VS Code. Companies are researched one at a time in the main session, following `docs/research-recipe.md`, in Batches whose size the owner sets (ADR 0011). Each company's rows go into `data/` and pass the check script before the next one starts.

## 1. Roster
`companies` lists every unique Portfolio company (about 130) with name, website, logo file, Fund (I or II), `is_highlight` and `is_exit`. The count matches the official page, duplicates are reported, and the owner has looked through it.

## 2. Pilot (Batch 1, 10 companies, one at a time)
Every field in `docs/data-model.md` is filled or recorded as missing: the Claims (description, long description, sub-sector, HQ now and at the first investment, year founded, status, business model, acquisition, founders, markets, accelerators, milestones) and every Round found, with or without Norte. Every Claim and Round has a source link, a Basis and a Confidence, and the company's `researched_on` date is set. The check script passes (required source links, valid URLs, allowed field values and formats, one value per field, USD sizes matching `fx.csv`, no duplicates), and the owner has reviewed all 10 and given feedback that is folded back into the process.

## 3. Scale-up
Remaining companies are researched one at a time, in Batches whose size the owner names (ADR 0011). Everything is gathered by agents. LinkedIn is read through Linked API only as the recipe's last step (ADR 0010); what is still not found is recorded as missing, and Norte's participation as `UNKNOWN`. Each Batch passes the check script and the owner spot-checks a sample. Done when every company in the Roster is covered. The owner may add new fields along the way.

## 4. Visualization v1
Built in this order: a throwaway prototype of the feel (Float drift, one Lens switch, two or three shell layouts), then the Sub-sector to Sector mapping (owner reviews), then `tools/logo-studio/` and all 130 logo circles (ADR 0015), then the real `site/` (ADR 0014).

Done when: the Float Lens runs with all 130 circle logos; the Sector Lens groups them into one ball per Sector with an icon and title, and back; spec in `.scratch/visualization-v1/spec.md`; the full navigation shell lists every Lens and View in IDEAS.md, with unbuilt ones greyed out, a disabled Receipts toggle and Play; clicking a Logo dot pauses it and opens the Company card (name, logo, Sector, short description, year founded, Fund); "Open full card" leads to a first-version Company profile showing everything in the Dataset (similar to the profile viewer, to be deepened after v1); every Lens, View and profile has a hash URL; the About panel and footer notice are in place, with a small note beside the notice saying the site works best on a desktop; and an explicit sync command copies the build into `mysite/public/vc-map/`.

Fixed constraints: static build output (ADR 0001, 0014); desktop-first, but the Float Lens, the Company card, the navigation shell and the simple Lenses work at 320px by tap, showing all 130 Logo dots at no less than a 14px radius (23px on desktop); on phones Float stays one fixed screen while grouped Lenses become a vertically scrollable stage; physics runs at a fixed 60 Hz step; shell layout and physics values come from the Float prototype's verdicts (`site/prototype-float/README.md` on branch `prototype/float`); unofficial notice; Estimated Claims visibly different everywhere, by one consistent convention explained in the About panel; works when copied into `mysite/public/vc-map/`.

## Later, out of v1
Deep Founder profiles (education, past roles, other companies): own plan and own ADR.
