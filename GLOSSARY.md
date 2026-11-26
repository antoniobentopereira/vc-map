# VC Map

An unofficial, static visual exploration of Norte Ventures and the companies it has invested in. Not affiliated with Norte Ventures.

## Language

**Firm**:
The venture capital firm being mapped. Norte Ventures for now; other firms may follow.
_Avoid_: VC, manager

**Fund**:
A pool of money the Firm raised and invests from (Fund I, Fund II). Each Portfolio company belongs to exactly one Fund.
_Avoid_: Vehicle

**Portfolio company**:
A company the Firm has invested in.
_Avoid_: Startup, investee

**Highlight**:
A Portfolio company the Firm itself features as a highlight. Marked on the company, not a separate group.
_Avoid_: Featured

**Exit**:
A Portfolio company the Firm lists as having left its portfolio (acquired or sold). Marked on the company, not a separate group.
_Avoid_: Sold company

**Founder**:
A person who started a Portfolio company. Someone who joined later, or who co-founded only a later holding company, is not a Founder. The Firm's thesis weighs founders heavily, so they will get their own detailed profile later.
_Avoid_: Entrepreneur, CEO

**Round**:
One funding event of a Portfolio company, whoever invested: its year, type (pre-seed, seed, Series A and so on, or debt), total size and investors. Recorded whether or not the Firm took part. The **last round** is the latest one that is not debt.
_Avoid_: Raise, deal

**Investment**:
A Round in which the Firm took part. A Portfolio company can have several; the earliest is the **first investment**, and any later one is a **follow-on**. Whether the Firm took part in a Round is true, false or unknown: the Firm is rarely named in press, so "not named" is unknown, never false.
_Avoid_: Deal, check

**Sub-sector**:
A detailed label for what market a Portfolio company serves, such as "Industrial predictive maintenance". Assigned to each company from its own description.
_Avoid_: Category, vertical

**Sector**:
A broad group of Sub-sectors, assigned once the whole portfolio has been classified. Defined in one mapping, never per company.
_Avoid_: Industry, vertical

**HQ**:
Where a Portfolio company says its headquarters is, as a city and country. Legal incorporation never counts. Recorded both now and at the first investment.
_Avoid_: Location, domicile

**Status**:
Whether a Portfolio company is operating: stealth, active, inactive or closed. Being acquired is not a status.
_Avoid_: State

**Acquisition**:
A Portfolio company being bought by another company. Recorded with the acquirer and year, separately from Status, because an acquired company may keep operating. Not the same as an Exit, which is the Firm's own listing.
_Avoid_: Sale, buyout

**Investment thesis**:
Our reasoned case for why a Portfolio company is worth backing: the problem, the logic of the business, the market and its reachable share, what makes it different, why it fits Norte, and the risks. It is mostly deduced, so it is an estimated Claim with its reasoning in the note, and it never states Norte's own reasoning as fact unless a Source says so.
_Avoid_: Pitch, rationale

**Milestone**:
A dated, non-funding event that tells a Portfolio company's story (a launch, pivot, new office, HQ move, accelerator, acquisition it makes, big customer, traction mark), written as a sentence or two that says why it mattered. Legal registration and holding-company restructurings are not Milestones. Milestones and Rounds together make its timeline.
_Avoid_: Event, history item

**Claim**:
A single fact about a Portfolio company, tied to one Source, with a Basis and a Confidence. A field holds one value: when Sources conflict, the most likely value is kept and the discarded ones are noted.
_Avoid_: Data point, fact

**Source**:
The public page, article or document a Claim comes from, referenced by its link.
_Avoid_: Reference, citation

**Basis**:
Whether a Claim is **Reported** (a Source states it) or **Estimated** (we deduced it, and the reasoning is shown). Estimated Claims are always displayed as visibly different from Reported ones.
_Avoid_: Type, kind

**Confidence**:
How sure we are of a Claim: high, medium or low.
_Avoid_: Accuracy, score

**Original logo**:
A Portfolio company's own brand logo, in its own colors, clearly representing the right company. Not a version recolored by the Firm or anyone else. It need not come from the company's own site, but where it was found is always recorded.
_Avoid_: Brand asset, official logo

**Logo origin**:
How an Original logo was obtained: from the company's own site, through a web search that led to a public source, or added by hand. Recorded with the page or file it was taken from.
_Avoid_: Logo source type

## Work stages

**Roster**:
The complete list of Portfolio companies, before any detail is gathered about them.
_Avoid_: Master list

**Batch**:
A group of Portfolio companies taken from the Roster and fully researched, one company after another. The owner sets its size.
_Avoid_: Wave, chunk

**Pilot**:
The first Batch, 10 companies, used to validate the process. The owner personally reviews it and gives feedback. Deliberately mixes well-documented companies with **hard cases** (thin public coverage, non-Brazilian, or an older Exit), so gaps show up before scale-up.
_Avoid_: Prototype, test run

**Dataset**:
The collected Portfolio companies, Claims and Rounds, with the exchange rates and the Sub-sector to Sector mapping they rely on. The output of the data-gathering part.
_Avoid_: Database

**Visualization**:
The static site built on the Dataset. The output of the visual part.
_Avoid_: Dashboard, app

## Visualization

**Logo dot**:
One Portfolio company's mark on the canvas, shown as its Original logo. Every Lens moves the same Logo dots; none are created or destroyed when switching Lens.
_Avoid_: Dot, bubble, node

**Lens**:
One way of arranging every Logo dot on the canvas, such as by Fund, Sector or Status. Switching Lens moves the dots from their current place to their new one.
_Avoid_: Layout, view, mode

**Company card**:
A small centered summary of one Portfolio company, opened by clicking its Logo dot, which stops moving while the card is open. It leads to the Company profile.
_Avoid_: Popup, tooltip, modal

**Company profile**:
A page holding everything the Dataset knows about one Portfolio company.
_Avoid_: Company page, full card, detail view

**View**:
A page of the Visualization that shows something other than one Logo dot per Portfolio company, such as the Norte Timeline (Rounds), the Investors views or the Quiz.
_Avoid_: Lens, screen, page
