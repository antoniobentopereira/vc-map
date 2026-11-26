import type { Field } from "./card-data";

export type Round = {
  year: number;
  type: string;
  size_usd: number | null;
  norte: boolean | null;
  co_investors: string[];
  basis: Field["basis"];
  confidence: string;
  source: string;
};
export type Milestone = Field & { date: string };
export type ProfileCompany = {
  slug: string;
  name: string;
  website: string;
  logo: string;
  fund: string;
  fields: Record<string, Field | undefined>;
  lists: { founders: Field[]; markets: Field[]; accelerators: Field[]; milestones: Milestone[] };
  rounds: Round[];
  first_investment: Round | null;
  follow_on: boolean | null;
};

const TYPE_LABELS: Record<string, string> = {
  angel: "Angel", pre_seed: "Pre-seed", seed: "Seed", series_a: "Series A", series_b: "Series B", series_c: "Series C",
  series_d: "Series D", series_e: "Series E", series_f_plus: "Series F+", unknown: "Round (type unknown)", debt: "Debt",
};

export function formatUsd(n: number): string {
  if (n >= 1e9) return `US$${+(n / 1e9).toFixed(1)}B`;
  if (n >= 1e6) return `US$${+(n / 1e6).toFixed(1)}M`;
  if (n >= 1e3) return `US$${Math.round(n / 1e3)}k`;
  return `US$${n}`;
}

export const norteLabel = (norte: boolean | null) => (norte === null ? "unknown" : norte ? "yes" : "no");

/** A Round as one traceable value: its own Basis, Confidence and Source. */
export function roundField(r: Round): Field {
  const size = r.size_usd === null ? "size not publicly available" : formatUsd(r.size_usd);
  return {
    value: `${TYPE_LABELS[r.type] ?? r.type} · ${size} · Norte took part: ${norteLabel(r.norte)}`,
    basis: r.basis,
    confidence: r.confidence,
    source: r.source,
  };
}

export type TimelineItem =
  | { kind: "milestone"; date: string; field: Field }
  | { kind: "round"; date: string; field: Field; round: Round };

/** Milestones and Rounds on one timeline, earliest first; within a tie the file order is kept. */
export function timeline(company: ProfileCompany): TimelineItem[] {
  const items: TimelineItem[] = [
    ...company.lists.milestones.map((m): TimelineItem => ({ kind: "milestone", date: m.date, field: m })),
    ...company.rounds.map((r): TimelineItem => ({ kind: "round", date: String(r.year), field: roundField(r), round: r })),
  ];
  return items
    .map((item, i) => ({ item, i }))
    .sort((a, b) => a.item.date.localeCompare(b.item.date) || a.i - b.i)
    .map(({ item }) => item);
}
