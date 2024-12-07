from collections.abc import Iterable
from typing import Optional, List


class ListNode(Iterable):
    def __iter__(self):
        for x in self.val:
            yield x

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp = None
        next_node = None
        while head:
            next_node = head.next
            head.next = temp
            temp = head
            head = next_node
        return temp
