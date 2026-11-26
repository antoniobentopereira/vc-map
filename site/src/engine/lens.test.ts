import { describe, expect, it } from "vitest";
import { layoutLens, type LensCompany, type Viewport } from "./lens";
import { SECTORS } from "../sectors";

const insets = { top: 0, right: 0, bottom: 0, left: 0 };
const sizes = [22, 19, 14, 14, 10, 10, 8, 8, 7, 7, 4, 4, 3]; // the real Sector counts
const sectorOf = (i: number) => SECTORS[sizes.findIndex((_, s) => i < sizes.slice(0, s + 1).reduce((a, b) => a + b, 0))].name;
const companies: LensCompany[] = Array.from({ length: 130 }, (_, i) => ({ fund: i < 79 ? "I" : "II", sector: sectorOf(i) }));
const bars = { top: 56, right: 0, bottom: 90, left: 0 };
const desktop: Viewport = { width: 1500, height: 900, insets: bars };
const phone: Viewport = { width: 320, height: 568, insets: { top: 56, right: 0, bottom: 110, left: 0 } };

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

describe("Sector Lens layout", () => {
  const dist = (a: { x: number; y: number }, b: { x: number; y: number }) => Math.hypot(a.x - b.x, a.y - b.y);

  it.each([desktop, phone])("lands each dot in its own Sector's ball", (viewport) => {
    const { targets, balls } = layoutLens("sector", companies, viewport);
    expect(balls).toHaveLength(SECTORS.length);
    companies.forEach((c, i) => {
      const ball = balls.find((b) => b.key === c.sector)!;
      expect(targets[i]).not.toBeNull();
      expect(dist(targets[i]!, ball)).toBeLessThanOrEqual(ball.radius);
    });
  });

  it.each([desktop, phone])("keeps balls apart from one another and from the bars", (viewport) => {
    const { balls, stageHeight } = layoutLens("sector", companies, viewport);
    for (const [i, a] of balls.entries()) {
      for (const b of balls.slice(i + 1)) expect(dist(a, b)).toBeGreaterThan(a.radius + b.radius);
      expect(a.x - a.radius).toBeGreaterThanOrEqual(viewport.insets.left);
      expect(a.x + a.radius).toBeLessThanOrEqual(viewport.width - viewport.insets.right);
      expect(a.y + a.radius).toBeLessThanOrEqual(stageHeight - viewport.insets.bottom);
    }
  });

  it.each([desktop, phone])("gives every Sector one title with an icon, above its ball and below the top bar", (viewport) => {
    const { decorations, balls } = layoutLens("sector", companies, viewport);
    expect(decorations).toHaveLength(SECTORS.length);
    for (const s of SECTORS) {
      const matches = decorations.filter((d) => d.text.startsWith(`${s.name} · `));
      expect(matches).toHaveLength(1);
      expect(matches[0].icon).toBe(s.icon);
      const ball = balls.find((b) => b.key === s.name)!;
      expect(matches[0].y).toBeLessThan(ball.y - ball.radius);
      expect(matches[0].y - 46).toBeGreaterThanOrEqual(viewport.insets.top);
    }
  });

  it("fits one screen on desktop and grows taller than the screen on a phone", () => {
    expect(layoutLens("sector", companies, desktop).stageHeight).toBe(desktop.height);
    expect(layoutLens("sector", companies, phone).stageHeight).toBeGreaterThan(phone.height);
  });

  it("stacks the phone balls in one column", () => {
    const { balls } = layoutLens("sector", companies, phone);
    expect(new Set(balls.map((b) => b.x)).size).toBe(1);
  });
});
