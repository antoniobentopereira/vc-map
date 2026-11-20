# The investment thesis is its own field, and it is an estimate

The owner wants to read a company's profile and understand its potential and why Norte backed it: the problem, the logic of the business, the size of the market and the share it can reach, what makes it different, and why it fits Norte. Most of that is reasoning, not reported fact, and part of it comes from research that is not about the company (industry reports, comparables).

We put it in a new single-value field, `investment_thesis`, instead of the long description. ADR 0003 says a deduced fact has Basis `estimated` and is shown in a visibly different colour so a guess never passes as a reported fact. A long description that mixed reported facts with a thesis could carry only one Basis, so it would either hide the guesses or mark the facts as guesses. Two fields keep both honest. The viewer shows the thesis directly under the long description.

Rules that keep it honest: the note shows the reasoning, including each market-size figure with its source or the arithmetic behind our own estimate; every page named was read; assumptions are labelled; Confidence is the weakest link; and Norte's own reasoning is never stated as fact unless a Source says it. Norte's Manifesto is the lens for the "fit" part, read as our interpretation. The recipe holds the how-to, not the check script, because a length or content check would reward padding.

We accept 3 to 6 more reads per company, and a field that is opinion by design, in exchange for a profile that explains why the company matters. The 13 researched companies get a thesis in a story pass (`/research-companies` with their names).
