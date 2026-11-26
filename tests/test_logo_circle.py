import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from logo_circle import SIZE, circle_path, open_logo, parse_crop, rebuild, render_circle  # noqa: E402

WHITE = "#ffffff"
RED = (255, 0, 0, 255)


def solid(width, height, color=RED):
    return Image.new("RGBA", (width, height), color)


class RenderCircleTest(unittest.TestCase):
    def test_is_512_px_with_transparent_corners(self):
        out = render_circle(solid(100, 100), (0, 0, 1, 1), WHITE)
        self.assertEqual(out.size, (SIZE, SIZE))
        for corner in ((0, 0), (SIZE - 1, 0), (0, SIZE - 1), (SIZE - 1, SIZE - 1)):
            self.assertEqual(out.getpixel(corner)[3], 0)
        self.assertEqual(out.getpixel((SIZE // 2, SIZE // 2))[3], 255)

    def test_fill_sits_behind_the_mark(self):
        mark = solid(100, 100, (0, 0, 0, 0))  # fully transparent mark: only the fill shows
        mark.paste((255, 0, 0, 255), (40, 40, 60, 60))
        out = render_circle(mark, (0, 0, 1, 1), "#0000ff")
        self.assertEqual(out.getpixel((SIZE // 2, SIZE // 2)), RED)
        self.assertEqual(out.getpixel((SIZE // 2, 40)), (0, 0, 255, 255))

    def test_square_mark_covers_the_circle(self):
        out = render_circle(solid(100, 100), (0, 0, 1, 1), WHITE)
        self.assertEqual(out.getpixel((SIZE // 2, 12)), RED)  # near the rim, still mark

    def test_wordmark_is_fitted_inside_the_circle(self):
        out = render_circle(solid(300, 100), (0, 0, 1, 1), WHITE)
        self.assertEqual(out.getpixel((SIZE // 2, SIZE // 2)), RED)
        self.assertEqual(out.getpixel((SIZE // 2, 12)), (255, 255, 255, 255))  # fill above the fitted mark
        left_edge = next(x for x in range(SIZE) if out.getpixel((x, SIZE // 2)) == RED)
        self.assertGreater(left_edge, 20)  # inside the circle, not touching the rim

    def test_crop_selects_part_of_the_source(self):
        source = solid(100, 100, (0, 0, 255, 255))
        source.paste(RED, (0, 0, 50, 100))
        out = render_circle(source, (0, 0, 0.5, 1), WHITE)
        self.assertEqual(out.getpixel((SIZE // 2, SIZE // 2)), RED)

    def test_crop_past_the_edges_adds_padding_around_the_mark(self):
        padded = render_circle(solid(100, 100), (-0.5, -0.5, 2, 2), WHITE)
        self.assertEqual(padded.getpixel((SIZE // 2, SIZE // 2)), RED)
        self.assertEqual(padded.getpixel((SIZE // 2, 40)), (255, 255, 255, 255))  # fill where the mark used to reach the rim
        self.assertEqual(padded.getpixel((SIZE // 2, SIZE // 4 + 12)), RED)  # the mark now spans half the circle

    def test_same_inputs_give_the_same_output(self):
        a = render_circle(solid(300, 100), (0, 0, 1, 1), "#123456")
        b = render_circle(solid(300, 100), (0, 0, 1, 1), "#123456")
        self.assertEqual(a.tobytes(), b.tobytes())


    def test_a_row_that_no_longer_has_a_fill_loses_its_circle_and_a_bad_row_does_not_stop_the_rest(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "site" / "logos").mkdir(parents=True)
            solid(64, 64).save(root / "site" / "logos" / "beta.png")
            (root / "site" / "logos" / "bad.png").write_bytes(b"not an image")
            old = root / circle_path("site/logos/beta.png")
            old.parent.mkdir(parents=True)
            old.write_bytes(b"old")
            rows = [
                {"name": "Bad", "logo": "site/logos/bad.png", "logo_background": "#ffffff", "logo_crop": ""},
                {"name": "Beta", "logo": "site/logos/beta.png", "logo_background": "dark", "logo_crop": ""},
                {"name": "Alpha", "logo": "site/logos/beta.png", "logo_background": "#000000", "logo_crop": ""},
            ]
            built, failed = rebuild(rows, root)
            self.assertEqual(built, ["Alpha"])
            self.assertEqual(len(failed), 1)
            self.assertTrue(failed[0].startswith("Bad"))

    def test_a_tiny_crop_still_renders(self):
        out = render_circle(solid(100, 100), (0.1, 0.1, 0.0001, 0.5), WHITE)
        self.assertEqual(out.size, (SIZE, SIZE))


class OpenLogoTest(unittest.TestCase):
    def test_svg_is_rasterized_with_transparency(self):
        svg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="20"><rect width="20" height="20" fill="#ff0000"/></svg>'
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "a.svg"
            path.write_text(svg, encoding="utf-8")
            image = open_logo(path).convert("RGBA")
        self.assertEqual(image.size, (1024, 512))
        self.assertEqual(image.getpixel((100, 256)), RED)
        self.assertEqual(image.getpixel((900, 256))[3], 0)


class ParseCropTest(unittest.TestCase):
    def test_fractions_and_empty(self):
        self.assertEqual(parse_crop("0.1,0.2,0.5,0.6"), (0.1, 0.2, 0.5, 0.6))
        self.assertEqual(parse_crop(""), (0, 0, 1, 1))


class RebuildTest(unittest.TestCase):
    def test_builds_a_webp_per_row_with_a_hex_background_only(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "site" / "logos").mkdir(parents=True)
            solid(64, 64).save(root / "site" / "logos" / "alpha.png")
            solid(64, 64).save(root / "site" / "logos" / "beta.png")
            rows = [
                {"name": "Alpha", "logo": "site/logos/alpha.png", "logo_background": "#ffffff", "logo_crop": "0,0,1,1"},
                {"name": "Beta", "logo": "site/logos/beta.png", "logo_background": "dark", "logo_crop": ""},
                {"name": "Gamma", "logo": "", "logo_background": "", "logo_crop": ""},
            ]
            built, failed = rebuild(rows, root)
            self.assertEqual((built, failed), (["Alpha"], []))
            with Image.open(root / circle_path("site/logos/alpha.png")) as circle:
                self.assertEqual(circle.size, (SIZE, SIZE))
            self.assertFalse((root / circle_path("site/logos/beta.png")).exists())


if __name__ == "__main__":
    unittest.main()
