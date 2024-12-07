from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_listnode(lst):
    dummy = ListNode()  # Dummy node
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse_list(head) -> ListNode:
            prev, current = None, head
            while current:
                next_node, current.next = current.next, prev
                prev, current = current, next_node
            return prev

        if not head or not head.next:
            return True

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        first_half = head
        second_half = reverse_list(slow.next)
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True

if __name__ == '__main__':
    t = Solution().isPalindrome(list_to_listnode([1, 2, 2, 1]))
    print(t)