# 04: Sector mapping

Spec: `.scratch/visualization-v1/spec.md`

**What to build:** Every Sub-sector in the Dataset belongs to a Sector, so the Company card and the Sector Lens can show one. Claude proposes the Sectors and the mapping, and the owner reviews and approves it before it is final (ADR 0006).

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent (HITL: owner approval required before closing)

- [ ] Claude proposes about 8 to 12 Sectors, each with an icon idea (a simple line icon in the ink color), and assigns a Sector to each of the 122 Sub-sectors in `sectors.csv`.
- [ ] The proposal is shown to the owner in a form easy to review (each Sector, its Sub-sectors and its company count) and adjusted until the owner approves.
- [ ] `sectors.csv` holds the approved mapping. The Sector list and icon choices are recorded where the Sector Lens can use them.
- [ ] `check_files` fails when any Sub-sector has no Sector. Tested with small CSVs.
- [ ] `docs/data-model.md` says a Sector is required.
- [ ] The Python tests and the data check pass.
