/** One value as the site data file carries it. */
export type Field = { value: string | number; basis: "reported" | "estimated"; confidence: string; source: string };

export const NOT_AVAILABLE = "not publicly available";
