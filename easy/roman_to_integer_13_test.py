import unittest
from roman_to_integer_13 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_III_equals_3(self):
        actual = self.s.roman_to_int("III")
        self.assertEqual(actual, 3)

    def test_VII_equals_7(self):
        actual = self.s.roman_to_int("VII")
        self.assertEqual(actual, 7)

    def test_IX_equals_9(self):
        actual = self.s.roman_to_int("IX")
        self.assertEqual(actual, 9)

    def test_MMCXL_2140(self):
        actual = self.s.roman_to_int("MMCXL")
        self.assertEqual(actual, 2140)
