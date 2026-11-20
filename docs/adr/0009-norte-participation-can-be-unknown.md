# Norte's participation in a Round can be unknown; founder, founding year and milestone rules tightened

Amends ADR 0005 (which had `norte_participated` as TRUE or FALSE) and refines ADR 0003.

The Pilot recorded "Norte not named in any Source" as `FALSE` with low Confidence. About 13 of 26 Rounds were wrong in that way: Norte is a follower investor that press articles rarely name, so absence from an article is weak evidence. It also made the derived first investment and follow-on silently wrong. `norte_participated` now takes `UNKNOWN`: `FALSE` is kept only for a Source that lists the Round's investors without Norte, and a derived follow-on is unknown while an `UNKNOWN` Round could still change it.

Three definitions the Pilot left open were fixed by the owner (2026-11-19):

- `year_founded` is the start of work, the earliest year the company counts itself as working, not its legal registration date (which goes in the note when it differs).
- A Founder is someone who started the company; joining later, or co-founding only a later holding company, does not count.
- Milestones are storytelling events. Legal registration, holdings and restructurings are not Milestones.

Company registry data (Brazil's CNPJ open data through BrasilAPI) is an accepted Source for opening dates, registered addresses and administrators, without an exact page link; a registered seat is only an Estimated HQ.

The owner decided (2026-11-19) that everything is gathered by agents and that the owner does not look things up or fill claims by hand. How agents read LinkedIn is in ADR 0010, which supersedes the LinkedIn decision first recorded here. The Pilot's Norma rows, which came from LinkedIn profiles the owner read by hand, stay as they are.
