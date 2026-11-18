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
A person who started a Portfolio company. The Firm's thesis weighs founders heavily, so they will get their own detailed profile later.
_Avoid_: Entrepreneur, CEO

**Investment**:
One event in which the Firm put money into a Portfolio company. A Portfolio company can have several.
_Avoid_: Deal, round

**Claim**:
A single fact about a Portfolio company or an Investment, tied to one Source, with a Basis and a Confidence.
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
A group of Portfolio companies taken from the Roster and fully researched together.
_Avoid_: Wave, chunk

**Pilot**:
The first Batch, 10 companies, used to validate the process. The owner personally reviews it and gives feedback.
_Avoid_: Prototype, test run

**Dataset**:
The collected Portfolio companies, Investments and Claims. The output of the data-gathering part.
_Avoid_: Database

**Visualization**:
The static site built on the Dataset. The output of the visual part.
_Avoid_: Dashboard, app
