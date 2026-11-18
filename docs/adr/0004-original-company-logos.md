# Logos show each company's original branding, with their origin recorded

Each Portfolio company's logo must be its Original logo: its own brand logo in its own colors. The Firm's portfolio page does not qualify, because it recolors every logo in the Firm's palette, which defeats the visual goal of the map. The Norte logos are reference material only (to spot an obviously wrong candidate) and are never a final value or a fallback.

Logos are found first by simple rules on the company's own homepage, then, for what remains, by an agent-run, search-assisted pass. Search is only a discovery step: no scraped image-search results, no paid search API, nothing scripted. A third-party source is fine if it yields a visually credible logo of the right company. A company with no credible logo keeps an empty logo, is listed for manual follow-up, and shows a neutral name placeholder on the site.

Every logo records its origin (`company-site`, `web-search` or `manual`) and the URL it came from, so each one can be traced, for example for a removal request. Logos are visual assets taken from credible public locations; they are not presented as official brand files, and the site keeps its removal-on-request notice (see ADR 0003).

## Exception: Glue

Glue (a stealth company) has no Original logo anywhere public. By the owner's decision (2026-11-18) it keeps the logo from the Firm's portfolio page, recolored in the Firm's palette, with `logo_origin` `manual` and the Norte URL as `logo_source`. This is the only company allowed a `norte.ventures` source (`NORTE_LOGO_EXCEPTIONS` in `scripts/check_data.py`). Replace it if an Original logo ever appears.
