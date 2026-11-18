# Ideas backlog

Data the owner wants later but that is not part of the current data model. Each entry says where the data would likely come from and how hard it is to collect.

## Headcount

How many people work at each company, ideally with a few points over time to show growth.

- **Likely sources:** LinkedIn company pages (an employee range, such as 201–500), press articles that mention team size, the company's careers or About page, the Y Combinator profile (team size for YC companies).
- **Difficulty:** medium to hard. LinkedIn shows only ranges and needs a login for detail; press figures are occasional and dated differently per company. Goes stale fast, so it needs an "as of" date.

## Valuation

The company's valuation at its latest Round, or at each Round.

- **Likely sources:** press coverage of large rounds (Brazil Journal, Bloomberg Línea, startups.com.br), unicorn lists, the company's own announcements.
- **Difficulty:** hard. Usually published only for large or late-stage companies, often as "more than R$1 billion" rather than an exact figure, and post-money and pre-money are rarely stated. Most early-stage companies will have no public valuation. Could fit as an extra column in `rounds.csv` (empty when undisclosed), converted to USD the same way as round sizes.
