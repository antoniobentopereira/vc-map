# The long description and the milestones carry the company's story

Amends ADR 0007 (one value per field) for the long description's sources, and `docs/data-model.md`'s rule "from one Source".

The owner reviewed the first 13 companies and found the long description (about 435 characters on average, against 176 for the short one) barely different from the short description, and the milestones too few to tell a story (one to six per company). The profile page is where the portfolio is understood, so these two fields now aim to be about ten times longer, as the sources allow: a connected profile of 1,500 to 4,500 characters and 8 to 15 dated milestones, each a sentence or two that says why it mattered.

A text that long cannot come from one page, so `source_url` holds the main page it draws on and the note names every other page used. Each page named must have been read (ADR 0003), and nothing is invented: a company with little public coverage keeps a short text. The rule is a target in the recipe, not a check-script rule, because a length check would reward padding.

We accept more reads per company (about 5 to 10 more) and a claim whose single Source link no longer covers every sentence, in exchange for profiles that read as a story. The first 13 companies keep their short texts until a story pass rewrites them (`/research-companies` with their names).
