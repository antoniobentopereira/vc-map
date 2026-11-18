# 02: Logos: one logo file per company

**What to build:** Each Portfolio company's logo is downloaded and stored in `site/`, and linked from its row in the companies CSV. The official portfolio page is tried first; if a logo is missing there, look on the company's own site, and if still missing, search the internet. A report lists any company still without a logo. The owner browses the logo folder and sees a logo for each company.

**Blocked by:** 01 (Roster).

**Status:** resolved

**Note:** The "portfolio page first" order below was superseded after review by tickets 09 and 10 (see ADR 0004): the portfolio logos use the Firm's palette, not each company's original branding.

- [ ] Every company row points to a logo file that exists
- [ ] The report names any company with no logo found, and where each logo came from
- [ ] File names are predictable and stable per company
