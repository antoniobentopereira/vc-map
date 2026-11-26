# 06: Company profile v1

Spec: `.scratch/visualization-v1/spec.md`

**What to build:** "Open full card" leads to a Company profile at `#/company/<slug>` showing everything the Dataset knows about the company, in the spirit of the internal profile viewer, with every value traceable to its Source. A keyboard or screen-reader user can reach every company by name.

**Blocked by:** 03, 05

**Status:** ready-for-agent

- [ ] The site data builder carries:
  - every single-value and list field as `{value, basis, confidence, source}`;
  - Rounds, each with its own provenance, its USD size and Norte's participation (true, false or unknown);
  - first investment and follow-on, from the existing derived views.
  - Notes are not shipped.
- [ ] The builder refuses to write the data file when the data check fails.
- [ ] Builder seam tests cover all of the above with small CSVs.
- [ ] The profile shows, in order:
  1. header: logo, name, Status, description;
  2. facts: Sector and Sub-sector, Status, business model, year founded, HQ now and at the first investment, Fund, and acquirer and acquisition year when acquired;
  3. long description;
  4. Investment thesis, labelled as our estimated reasoning;
  5. Founders, markets and accelerators;
  6. one timeline of Milestones and Rounds, with Rounds styled differently;
  7. record details: website and Fund.
- [ ] Every value links to its Source, Estimated values use the convention, and empty fields read "not publicly available".
- [ ] There is a way back to the dots, and a shared `#/company/<slug>` link opens straight on the profile.
- [ ] A visually hidden, keyboard-reachable list of every company links to each profile.
- [ ] Reads well at 320px. Checked in the browser.
