import unittest
from easy.reverse_linked_list_206 import Solution, ListNode


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_if_list_is_empty_should_return_none(self):
        empty_list = None
        self.assertIsNone(self.s.reverse_list(empty_list))

    def test_reverse_list(self):
        node =  [1, 2, 3, 4, 5]
        self.assertEqual(self.s.reverse_list(node), [5, 4, 3, 2, 1])