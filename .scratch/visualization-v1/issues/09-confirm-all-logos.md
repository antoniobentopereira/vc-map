# 09: Confirm all 130 logo circles

Spec: `.scratch/visualization-v1/spec.md`

**What to build:** Every Portfolio company has a confirmed logo circle, chosen by the owner in the logo studio, and the transition period for `logo_background` ends.

**Blocked by:** 08

**Status:** ready-for-human

- [ ] The owner has confirmed all 130 logos in the studio. Every row has a `logo_crop` and a hex `logo_background`.
- [ ] The check script no longer accepts `dark` / `light` / `both`. The tests and `docs/data-model.md` are updated.
- [ ] The site shows a circle for every company, and no raw-logo fallback is still in use.
