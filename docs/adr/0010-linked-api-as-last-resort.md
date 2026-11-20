# LinkedIn is read through Linked API, read-only and as a last resort

Amends ADR 0003 (no paid platforms) and supersedes the LinkedIn paragraph of ADR 0009.

The Pilot showed that some facts are only on LinkedIn: founders and founding year for thin companies (Norma), the headquarters as the company states it, and above all the round posts that tag every investor, which is where Norte, a follower investor the press rarely names, shows up. Agents cannot read LinkedIn directly (403), and the owner decided (2026-11-19) not to look things up by hand. So the owner subscribed to Linked API, which runs workflows in a cloud browser signed in to the owner's own LinkedIn account.

It is the last step of the research recipe, used only for a field still missing, or a Round whose Norte participation is still `UNKNOWN`, after the free public sources and the stop rule. It goes through one client, `scripts/linkedin.py`, which reads its two tokens from environment variables (never the repo) and refuses any workflow containing an action that is not a read, so no agent can message, connect, react, comment or post from the owner's account. Each company gets at most 4 workflows.

We accept the trade-offs knowingly. Automating a LinkedIn account is against LinkedIn's terms, and Linked API does not promise that accounts are never restricted; the owner chose this for their own account. Opening a profile can show the owner's name to that person. Usage counts against the account's LinkedIn limits, which the owner sets in the Linked API platform. A Claim from it cites the public LinkedIn URL of the page or post read, like any other Source.
