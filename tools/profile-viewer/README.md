# Profile viewer

A throwaway, read-only page for reviewing one Portfolio company's research at a time. See `docs/adr/0008-profile-viewer-is-disposable.md`.

1. Generate the data: `python tools/profile-viewer/build_data.py` (rerun after editing any CSV in `data/`).
2. Open `tools/profile-viewer/index.html` by double-click. No server needed.

Pick a company from the search box or step with the arrows; the choice lives in the URL hash. Only companies with a Claim or Round row, or `researched_on` set, are listed. The script writes only `tools/profile-viewer/data.js`, which is gitignored.
