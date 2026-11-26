import csv
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from check_data import COMPANY_COLUMNS  # noqa: E402
from logo_circle import SIZE, circle_path  # noqa: E402

spec = importlib.util.spec_from_file_location("logo_studio_serve", ROOT / "tools" / "logo-studio" / "serve.py")
studio = importlib.util.module_from_spec(spec)
spec.loader.exec_module(studio)


def row(name, logo="site/logos/a.png", **extra):
    base = {c: "" for c in COMPANY_COLUMNS}
    base.update(name=name, website="https://x.test", fund="I", is_highlight="FALSE", is_exit="FALSE", logo=logo,
                logo_origin="manual", logo_source="https://x.test/a.png", researched_on="2026-01-01")
    base.update(extra)
    return base


class SaveChoiceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)
        (self.root / "data").mkdir()
        (self.root / "site" / "logos").mkdir(parents=True)
        Image.new("RGBA", (100, 50), (255, 0, 0, 255)).save(self.root / "site" / "logos" / "a.png")
        self.csv = self.root / "data" / "companies.csv"
        self.rows = [row("Alpha", website="https://alpha.test"), row("Beta", logo="", logo_background="")]
        with open(self.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COMPANY_COLUMNS)
            w.writeheader()
            w.writerows(self.rows)

    def read(self):
        with open(self.csv, newline="", encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))

    def test_writes_only_the_two_columns_and_renders_the_circle(self):
        studio.save_choice("Alpha", "0.1,0.1,0.5,0.5", "#112233", self.csv, self.root)
        after = self.read()
        self.assertEqual(after[0]["logo_crop"], "0.1,0.1,0.5,0.5")
        self.assertEqual(after[0]["logo_background"], "#112233")
        changed = {c for c in COMPANY_COLUMNS if after[0][c] != self.rows[0][c]}
        self.assertEqual(changed, {"logo_crop", "logo_background"})
        self.assertEqual(after[1], self.rows[1])
        self.assertEqual(Image.open(self.root / circle_path("site/logos/a.png")).size, (SIZE, SIZE))

    def test_empty_crop_means_the_whole_image(self):
        studio.save_choice("Alpha", "", "#ffffff", self.csv, self.root)
        self.assertEqual(self.read()[0]["logo_crop"], "")

    def test_refuses_bad_input_and_leaves_the_file_alone(self):
        before = self.csv.read_bytes()
        for name, crop, color in [("Alpha", "0,0,4,1", "#ffffff"), ("Alpha", "", "white"), ("Alpha", "", "dark"),
                                  ("Nobody", "", "#ffffff"), ("Beta", "", "#ffffff")]:
            with self.assertRaises(ValueError, msg=(name, crop, color)):
                studio.save_choice(name, crop, color, self.csv, self.root)
        self.assertEqual(self.csv.read_bytes(), before)
        self.assertEqual(list(self.csv.parent.glob("*.tmp")), [])

    def test_a_logo_that_cannot_render_leaves_the_file_alone(self):
        (self.root / "site" / "logos" / "a.png").write_bytes(b"not an image")
        before = self.csv.read_bytes()
        with self.assertRaises(ValueError):
            studio.save_choice("Alpha", "", "#ffffff", self.csv, self.root)
        self.assertEqual(self.csv.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
