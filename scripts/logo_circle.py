"""Render a Portfolio company's logo circle from its Original logo (ADR 0015).

`render_circle(image, crop, background)` is the one renderer; `main()` rebuilds every circle from
data/companies.csv (`logo_crop`, `logo_background`). Needs Pillow (imported only when rendering); SVG logos also need cairosvg.
"""
import csv
import io
import re
from pathlib import Path

SIZE = 512
WIDE_RATIO = 1.25  # marks at least this far from square are fitted, not covered
SAFE_RADIUS = 0.85  # fitted marks stay inside this share of the circle's radius
SUPERSAMPLE = 4

ROOT = Path(__file__).resolve().parent.parent
COMPANIES_CSV = ROOT / "data" / "companies.csv"
CIRCLE_DIR = Path("site") / "logos" / "circles"
HEX = re.compile(r"#[0-9a-fA-F]{6}")


def parse_crop(text):
    """'x,y,w,h' as fractions of the source image; empty means the whole image."""
    if not text:
        return (0.0, 0.0, 1.0, 1.0)
    x, y, w, h = (float(part) for part in text.split(","))
    return (x, y, w, h)


def circle_path(logo):
    """Where the circle for a logo file lives (relative to the repo root), e.g. site/logos/circles/alpha.webp."""
    return CIRCLE_DIR / f"{Path(logo).stem}.webp"


def render_circle(source, crop, background):
    """A SIZE x SIZE RGBA circle: the cropped mark on a `#rrggbb` fill, transparent outside the circle."""
    from PIL import Image, ImageDraw

    x, y, w, h = crop
    width, height = source.size
    left, top = round(x * width), round(y * height)
    box = (left, top, max(round((x + w) * width), left + 1), max(round((y + h) * height), top + 1))  # at least 1px
    mark = source.convert("RGBA").crop(box)

    fill = tuple(int(background[i:i + 2], 16) for i in (1, 3, 5))
    canvas = Image.new("RGBA", (SIZE, SIZE), fill + (255,))

    ratio = mark.width / mark.height
    if max(ratio, 1 / ratio) >= WIDE_RATIO:
        # Fit: the mark's rectangle fits inside the safe inner circle.
        diagonal = 2 * SAFE_RADIUS * SIZE / 2
        scale = diagonal / (mark.width ** 2 + mark.height ** 2) ** 0.5
    else:
        scale = SIZE / min(mark.width, mark.height)  # cover
    new_size = (max(1, round(mark.width * scale)), max(1, round(mark.height * scale)))
    mark = mark.resize(new_size, Image.LANCZOS)
    layer = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    layer.paste(mark, ((SIZE - new_size[0]) // 2, (SIZE - new_size[1]) // 2))  # a covering mark overhangs; the circle trims it
    canvas.alpha_composite(layer)

    big = SIZE * SUPERSAMPLE
    mask = Image.new("L", (big, big), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, big - 1, big - 1), fill=255)
    canvas.putalpha(mask.resize((SIZE, SIZE), Image.LANCZOS))
    return canvas


def save_circle(image, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "WEBP", lossless=True, method=6)


def open_logo(path):
    """The logo as an image, or None when it cannot be read (an SVG without cairosvg)."""
    from PIL import Image

    if path.suffix.lower() == ".svg":
        try:
            import cairosvg
        except ImportError:
            return None
        return Image.open(io.BytesIO(cairosvg.svg2png(url=str(path), output_width=1024)))
    return Image.open(path)


def has_circle_choice(row):
    """Only a logo with a `#rrggbb` fill gets a circle."""
    return bool(row["logo"]) and bool(HEX.fullmatch(row["logo_background"]))


def rebuild(rows, root=ROOT):
    """Regenerate the circle of every row with a `#rrggbb` logo_background and delete the circles of the others.

    Returns (built, skipped, failed) company names: skipped are SVGs without cairosvg, failed could not be rendered."""
    built, skipped, failed = [], [], []
    for row in rows:
        if not has_circle_choice(row):
            if row["logo"]:
                (root / circle_path(row["logo"])).unlink(missing_ok=True)
            continue
        try:
            image = open_logo(root / row["logo"])
            if image is None:
                skipped.append(row["name"])
                continue
            save_circle(render_circle(image, parse_crop(row.get("logo_crop", "")), row["logo_background"]), root / circle_path(row["logo"]))
            built.append(row["name"])
        except Exception as error:  # one bad logo must not stop the rest
            failed.append(f"{row['name']} ({error})")
    return built, skipped, failed


def main():
    with COMPANIES_CSV.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    built, skipped, failed = rebuild(rows)
    print(f"Rebuilt {len(built)} logo circle(s).")
    if skipped:
        print(f"Skipped {len(skipped)} SVG logo(s) (install cairosvg to render them): {', '.join(skipped)}")
    if failed:
        print(f"Failed {len(failed)}: {'; '.join(failed)}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
