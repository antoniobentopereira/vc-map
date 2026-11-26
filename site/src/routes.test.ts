import { describe, expect, it } from "vitest";
import { hashOf, parseHash, type Known, type Route } from "./routes";

const known: Known = {
  lenses: ["float", "sector"],
  views: ["investors"],
  companies: ["tempo", "credaluga"],
};
const float: Route = { kind: "lens", id: "float" };

describe("routes", () => {
  it.each<Route>([
    { kind: "lens", id: "float" },
    { kind: "lens", id: "sector" },
    { kind: "view", id: "investors" },
    { kind: "company", slug: "tempo" },
  ])("round trips %o", (route) => {
    expect(parseHash(hashOf(route), known)).toEqual(route);
  });

  it("writes Float as #/", () => {
    expect(hashOf(float)).toBe("#/");
  });

  it.each(["", "#", "#/", "#/float"])("reads %j as Float", (hash) => {
    expect(parseHash(hash, known)).toEqual(float);
  });

  it.each(["#/nope", "#/status", "#/exit-wall", "#/company/ghost", "#/company/", "#/company/tempo/x", "#/sector/x", "garbage"])(
    "resolves unknown or unbuilt %j to Float",
    (hash) => {
      expect(parseHash(hash, known)).toEqual(float);
    },
  );

  it("ignores a trailing slash", () => {
    expect(parseHash("#/sector/", known)).toEqual({ kind: "lens", id: "sector" });
  });
});
