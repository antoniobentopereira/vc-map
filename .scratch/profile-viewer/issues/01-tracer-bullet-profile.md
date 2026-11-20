# 01: Tracer bullet: generate data and open a company profile

**What to build:** A generator script (Python standard library only) reads the CSVs in `data/` and writes a gitignored data file. The profile viewer page, opened by double-click from `tools/profile-viewer/`, lets me pick a researched Portfolio company (at least one Claim or Round row, or `researched_on` set) from a searchable list, in roster order, with the choice kept in the URL hash and previous/next buttons. It shows the logo (placeholder if none), name, short description (serif italic), long description and the Facts box in its fixed order (Sub-sector and Sector, Status, business model, year founded, HQ now, HQ at first investment, acquirer, acquisition year) with plain values. Style follows the spec: off-white background, thin dark borders, small uppercase labels, clarity over polish. Also add a small README with the rerun command, `.gitignore` for the generated file, and ADR 0008 (viewer is disposable, outside `site/`, its generated file is not a source of truth).

**Reference:** the owner's rough mockup is `.scratch/profile-viewer/mockup.png`: a loose guide to layout and mood only, no placeholder text reused.

**Blocked by:** None (can start immediately).

**Status:** resolved

- [x] Running the documented command produces the data file; opening the page by double-click works with no server
- [x] The picker lists only researched or started companies, supports search, URL hash and previous/next
- [x] Logo, name, short and long description and the Facts box show for a real company such as Tractian
- [x] Nothing is written to `data/` or `site/`; the generated file is gitignored
- [x] README holds the rerun command; ADR 0008 is written
