# 11: Release v1

Spec: `.scratch/visualization-v1/spec.md`

**What to build:** After a final check against the stage 4 definition of done, the finished v1 is copied into the personal site with one deliberate command.

**Blocked by:** 06, 09, 10

**Status:** ready-for-agent (HITL: owner signs off the visual pass)

- [ ] An explicit sync command copies the built static folder into `mysite/public/vc-map/`. It never runs on save or on build (ADR 0001).
- [ ] The synced folder works when opened from the personal site: relative paths, logos and the data file all load.
- [ ] A visual pass at about 1500px and 320px against the prototype verdicts, signed off by the owner.
- [ ] Every item of the stage 4 definition of done in `docs/stages.md` is met.
- [ ] `STATUS.md` is updated: v1 released and the next phase noted.
