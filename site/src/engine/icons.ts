import type { Graphics } from "pixi.js";

/** Simple line icons for the Sector Lens, drawn in a 24x24 box centered on (0, 0), in the given color. */
export function drawIcon(g: Graphics, name: string, color: number, size = 26) {
  const k = size / 24;
  const P = (x: number, y: number): [number, number] => [(x - 12) * k, (y - 12) * k];
  const line = (...pts: number[][]) => {
    g.moveTo(...P(pts[0][0], pts[0][1]));
    for (const p of pts.slice(1)) g.lineTo(...P(p[0], p[1]));
  };
  const circle = (x: number, y: number, r: number) => {
    const [cx, cy] = P(x, y);
    g.moveTo(cx + r * k, cy).circle(cx, cy, r * k);
  };
  const rect = (x: number, y: number, w: number, h: number) => {
    const [rx, ry] = P(x, y);
    g.roundRect(rx, ry, w * k, h * k, 2 * k);
  };
  switch (name) {
    case "spark": // four-point star
      line([12, 2], [14.5, 9.5], [22, 12], [14.5, 14.5], [12, 22], [9.5, 14.5], [2, 12], [9.5, 9.5], [12, 2]);
      break;
    case "bank-columns":
      line([3, 9], [12, 3], [21, 9], [3, 9]);
      for (const x of [6, 10, 14, 18]) line([x, 11], [x, 18]);
      line([3, 21], [21, 21]);
      break;
    case "browser-window":
      rect(3, 4, 18, 16);
      line([3, 9], [21, 9]);
      break;
    case "coins-arrow":
      circle(9, 9, 6);
      line([9, 6], [9, 12]);
      line([14, 17], [21, 17]);
      line([18.5, 14.5], [21, 17], [18.5, 19.5]);
      break;
    case "rising-line":
      line([3, 18], [9, 12], [13, 15], [21, 6]);
      line([15, 6], [21, 6], [21, 12]);
      break;
    case "heart-pulse":
      line([12, 20], [4, 12], [3.5, 8], [6.5, 5], [10, 5.5], [12, 8], [14, 5.5], [17.5, 5], [20.5, 8], [20, 12], [12, 20]);
      line([6, 12], [10, 12], [11.5, 9], [13, 15], [14.5, 12], [18, 12]);
      break;
    case "shopping-bag":
      line([5, 8], [19, 8], [20, 21], [4, 21], [5, 8]);
      line([9, 11], [9, 6], [10.5, 3.5], [13.5, 3.5], [15, 6], [15, 11]);
      break;
    case "megaphone":
      line([3, 10], [8, 10], [18, 5], [18, 19], [8, 14], [3, 14], [3, 10]);
      line([7, 14], [8.5, 20], [11.5, 20], [10.5, 15.5]);
      line([20.5, 10], [22, 10]);
      line([20.5, 14], [22, 14]);
      break;
    case "graduation-cap-briefcase":
      line([2, 9], [12, 4], [22, 9], [12, 14], [2, 9]);
      line([6, 11.5], [6, 16], [12, 19], [18, 16], [18, 11.5]);
      line([22, 9], [22, 15]);
      break;
    case "shield":
      line([12, 3], [20, 6], [20, 12], [17, 18], [12, 21], [7, 18], [4, 12], [4, 6], [12, 3]);
      line([8.5, 12], [11, 14.5], [15.5, 9.5]);
      break;
    case "bolt":
      line([13, 2], [5, 13], [11, 13], [10, 22], [19, 10], [13, 10], [13, 2]);
      break;
    case "truck-route":
      rect(2, 6, 12, 10);
      line([14, 9], [19, 9], [22, 12.5], [22, 16], [14, 16]);
      circle(7, 18, 2);
      circle(17.5, 18, 2);
      break;
    case "lifebuoy":
      circle(12, 12, 9);
      circle(12, 12, 4);
      line([5.6, 5.6], [9.2, 9.2]);
      line([18.4, 5.6], [14.8, 9.2]);
      line([5.6, 18.4], [9.2, 14.8]);
      line([18.4, 18.4], [14.8, 14.8]);
      break;
    default:
      circle(12, 12, 8);
  }
  g.stroke({ width: 1.6, color, cap: "round", join: "round" });
}
