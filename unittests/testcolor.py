import unittest

import renpy
from renpy.color import Color

class TestColor(unittest.TestCase):
    def test_hex_initialization(self):
        c = Color("#ff0000")
        self.assertEqual(c.rgba, (1.0, 0.0, 0.0, 1.0))
        self.assertEqual(c.hexcode, "#ff0000")

    def test_tuple_initialization(self):
        c = Color((0, 255, 0, 127))
        self.assertEqual(c.rgba, (0.0, 1.0, 0.0, 127/255.0))
        self.assertEqual(c.hexcode, "#00ff007f")

    def test_opacity(self):
        c = Color((255, 255, 255)).opacity(0.5)
        self.assertEqual(c.alpha, 127/255.0)

    def test_hls(self):
        c = Color("#ff0000")
        # Hue is 0, lightness is 0.5, saturation is 1.0
        self.assertEqual(c.hls, (0.0, 0.5, 1.0))

if __name__ == "__main__":
    unittest.main()
