import unittest
from easy.longest_common_prefix_14 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_the_longest_common_prefix_is_fl(self):
        prefix = "fl"
        strs = ["flower","flow","flight"]
        self.assertEqual(self.s.longest_common_prefix(strs), prefix)

    def test_the_longest_common_prefix_is_anti(self):
        prefix = "anti"
        strs = ["antihero","antidot","antimater", "antifox"]
        self.assertEqual(self.s.longest_common_prefix(strs), prefix)

    def test_the_longest_common_prefix_does_not_exist(self):
        prefix = ""
        strs = ["cat", "dog", "mouse", "fox"]
        self.assertEqual(self.s.longest_common_prefix(strs), prefix)