// What the navigation shell lists. Only built entries are enabled; the rest are visible but greyed,
// so visitors see where the project is heading.

export type LensEntry = { id: string; label: string; built: boolean };
export type ViewEntry = { id: string; label: string; built: boolean };

export const LENSES: LensEntry[] = [
  { id: "float", label: "Float", built: true },
  { id: "fund", label: "Fund", built: true },
  { id: "sector", label: "Sector", built: false },
  { id: "status", label: "Status", built: false },
  { id: "country", label: "Country", built: false },
  { id: "founding-year", label: "Founding year", built: false },
  { id: "money-raised", label: "Money raised", built: false },
  { id: "employee-count", label: "Employee count", built: false },
  { id: "business-model", label: "Business model", built: false },
];

export const VIEWS: ViewEntry[] = [
  { id: "norte-timeline", label: "Norte Timeline", built: false },
  { id: "investors", label: "Investors", built: false },
  { id: "theme-explorer", label: "Theme Explorer", built: false },
  { id: "how-early", label: "How early does Norte get in?", built: false },
  { id: "exit-wall", label: "Exit Wall", built: false },
  { id: "founder-graph", label: "Founder graph", built: false },
];
