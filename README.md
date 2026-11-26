# VC Map

An unofficial, static visual exploration of Norte Ventures and its portfolio.

Status: data gathering. The roster of about 130 portfolio companies and their logos are done, the Pilot (10 companies) plus three more are researched in `data/`, and the rest are researched one company at a time (see `docs/stages.md`). The visualization comes after a couple of batches.


## Running instructions

Node lives in `C:\Program Files\nodejs`; in PowerShell use `npm.cmd`. Run the `npm` commands from `site/`.

**Develop** (all work happens here, never in `mysite`):

```
cd site
npm run dev        # local dev server
npm run test       # Vitest
npm run typecheck
```

**Release to the personal site** (when a version is ready to ship):

```
python scripts/check_data.py     # from the repo root: data must pass
cd site
npm run data       # rebuild the site's JSON from data/
npm run build      # typecheck + build into site/dist/
npm run sync       # copy site/dist/ into ../mysite/public/vc-map/
```

Then commit and deploy in the `mysite` repo. `sync` deletes and replaces `mysite/public/vc-map/` each time, so never edit it by hand. It is never run automatically (ADR 0001). Adding a link to the site on the mysite homepage is done in `mysite`.

**Checks** (a pre-commit hook runs the first two; enable it once with `git config core.hooksPath .githooks`):

```
python -m unittest discover -s tests
python scripts/check_data.py
```
