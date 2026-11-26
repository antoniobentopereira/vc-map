# 03: Addresses and About panel

Spec: `.scratch/visualization-v1/spec.md`

**What to build:**
- Every Lens, View and Company profile has a shareable hash address.
- The browser's back button undoes navigation.
- Broken links land on Float.
- The `?` button opens an About panel that explains the project and the Estimated convention.

**Blocked by:** 02

**Status:** ready-for-agent

- [ ] A routes module maps `#/`, `#/<lens>`, `#/<view>` and `#/company/<slug>` to app state and back. Unknown or unbuilt addresses resolve to Float.
- [ ] Vitest covers the routes seam: round trips for Lenses, Views and company slugs, and unknown or unbuilt addresses resolving to Float.
- [ ] Switching Lens updates the address. Loading an address restores that state, and back and forward follow the browser history.
- [ ] `?` opens the About panel, which covers:
  - that the project is unofficial and not affiliated with Norte Ventures;
  - why it was built, and that it was built with AI;
  - the Estimated convention: muted dotted underline, "≈" before numbers, dashed outlines on shapes, with Basis and Confidence explained.
- [ ] The About panel closes by clicking outside it, with a close button or with Escape, and reads well at 320px.
