import unittest
from medium.sort_colors_75 import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_sort_colors(self):
        colors = [1, 2, 0, 2, 1, 0]
        self.s.sortColors(colors)
        self.assertEqual(colors, [0, 0, 1, 1, 2, 2])

    def test_sort_two_colors(self):
        two_colors = [2, 0, 2, 0]
        self.s.sortColors(two_colors)
        self.assertEqual(two_colors, [0, 0, 2, 2])

    def test_empty_colors(self):
        empty = []
        self.s.sortColors(empty)
        self.assertEqual(empty, [])

    def test_single_color_array(self):
        color = [1, 1, 1]
        self.s.sortColors(color)
        self.assertEqual(color, [1, 1, 1])