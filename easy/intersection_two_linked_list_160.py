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
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if not headA or not headB:
        #     return "No intersection"
        # int_a = headA
        # int_b = headB
        # while int_a != int_b:
        #     int_a = int_a.next if int_a else headB
        #     int_b = int_b.next if int_b else headA
        # return int_a if int_a else "No intersection"
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            setA = set()
            current = headA
            while current:
                setA.add(current)
                current = current.next
            current = headB
            while current:
                if current in setA:
                    return current
                current = current.next
            return None


if __name__ == '__main__':
    t = Solution().getIntersectionNode(list_to_listnode([4, 1, 8, 4, 5]), list_to_listnode([5, 6, 1, 8, 4, 5]))
    # t = Solution().getIntersectionNode(list_to_listnode([2,6,4]), list_to_listnode([1,5]))
    print(t)