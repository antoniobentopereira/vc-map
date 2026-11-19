# The profile viewer is disposable, lives outside `site/`, and its data file is not a source

`tools/profile-viewer/` is an internal page for reviewing the Pilot's research one company at a time. It is not the Visualization (stage 4) and not a preview of its design.

It lives outside `site/`, so it never ships with the static output (ADR 0001). It reads `data/` and `site/logos/` and writes nothing to either. Its generator writes one gitignored file, `data.js`, because a `file://` page cannot fetch CSVs. That file is a derivative: the CSVs stay the single source of truth (ADR 0002), and the page is read-only, so edits happen in the CSVs and the generator is rerun.

Whether stage 4 reuses any of it is decided later; until then the tool can be rewritten or deleted without ceremony.
