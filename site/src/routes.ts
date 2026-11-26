// Hash addresses <-> app state. Unknown or unbuilt addresses resolve to Float.

export type Route =
  | { kind: "lens"; id: string }
  | { kind: "view"; id: string }
  | { kind: "company"; slug: string };

/** What exists right now: built Lens and View ids and company slugs. */
export type Known = { lenses: string[]; views: string[]; companies: string[] };

const FLOAT: Route = { kind: "lens", id: "float" };

export function hashOf(route: Route): string {
  if (route.kind === "company") return `#/company/${encodeURIComponent(route.slug)}`;
  if (route.kind === "lens" && route.id === "float") return "#/";
  return `#/${route.id}`;
}

export function parseHash(hash: string, known: Known): Route {
  const parts = hash.replace(/^#\/?/, "").split("/").filter(Boolean).map(decode);
  if (parts.length === 0) return FLOAT;
  if (parts.length === 1) {
    const [id] = parts;
    if (known.lenses.includes(id)) return { kind: "lens", id };
    if (known.views.includes(id)) return { kind: "view", id };
  }
  if (parts.length === 2 && parts[0] === "company" && known.companies.includes(parts[1])) {
    return { kind: "company", slug: parts[1] };
  }
  return FLOAT;
}

function decode(s: string): string {
  try {
    return decodeURIComponent(s);
  } catch {
    return s;
  }
}
