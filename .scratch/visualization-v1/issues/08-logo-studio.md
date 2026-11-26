# 08: Logo studio

Spec: `.scratch/visualization-v1/spec.md`

**What to build:** A local logo studio walks the owner through each logo in four steps (crop, pick fill, preview, confirm) and saves the choices so the circles can always be rebuilt. It replaces the logo viewer. Like the profile viewer, it is disposable, lives outside `site/` and writes only its own columns (ADR 0008, ADR 0015).

**Blocked by:** 07

**Status:** done

- [x] It starts with one command as a local server page.
- [x] **Crop:** drag a box over the raw logo to strip away padding and borders.
- [x] **Fill:** use the eyedropper on the logo, or pick a preset (white, cream, Norte brown, black). The first suggestion comes from the old legibility word: `dark` suggests a dark fill, and `light` or `both` suggest white.
- [x] **Preview:** the circle on the cream surface with its ring, at the real desktop and phone dot sizes, updating live.
- [x] **Confirm:** writes `logo_crop` and `logo_background` (hex) to `companies.csv` atomically, touching no other column, and renders the circle through the renderer.
- [x] A filter shows only the logos not yet confirmed.
- [x] The save path is tested the same way as the logo viewer's CSV write.
- [x] `tools/logo-viewer/` is removed, and its README is replaced by the studio's.
