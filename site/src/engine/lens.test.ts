import { describe, expect, it } from "vitest";
import { layoutLens, type Viewport } from "./lens";

const insets = { top: 0, right: 0, bottom: 0, left: 0 };
const companies = Array.from({ length: 130 }, (_, i) => ({ fund: i < 79 ? "I" : "II" }));
const desktop: Viewport = { width: 1500, height: 900, insets };
const phone: Viewport = { width: 320, height: 568, insets };

describe("Float Lens layout", () => {
  it.each([desktop, phone])("gives every dot no target and a stage as tall as the viewport", (viewport) => {
    const layout = layoutLens("float", companies, viewport);
    expect(layout.targets).toHaveLength(130);
    expect(layout.targets.every((t) => t === null)).toBe(true);
    expect(layout.stageHeight).toBe(viewport.height);
    expect(layout.decorations).toEqual([]);
  });
});

describe("Fund Lens layout", () => {
  it.each([desktop, phone])("gives every dot one target and one titled ball per Fund", (viewport) => {
    const layout = layoutLens("fund", companies, viewport);
    expect(layout.targets).toHaveLength(130);
    expect(layout.targets.every((t) => t !== null)).toBe(true);
    expect(layout.decorations.map((d) => d.text)).toEqual(["Fund I · 79", "Fund II · 51"]);
    expect(layout.stageHeight).toBe(viewport.height);
  });

  it("puts the Funds side by side on a wide viewport and stacked on a tall one", () => {
    const [a, b] = layoutLens("fund", companies, desktop).decorations;
    expect(a.x).toBeLessThan(b.x);
    const [c, d] = layoutLens("fund", companies, phone).decorations;
    expect(c.y).toBeLessThan(d.y);
    expect(c.x).toBeCloseTo(d.x);
  });
});
