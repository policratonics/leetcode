from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def list_to_tree(lst):
        if not lst:  # Handle the case where the list is empty
            return None

        root = TreeNode(lst[0])  # The first element is the root
        queue = deque([root])  # Use a queue to build the tree level by level
        i = 1  # Start from the second element in the list

        while queue and i < len(lst):
            current = queue.popleft()  # Get the current node from the queue

            # Assign the left child
            if lst[i] is not None:
                current.left = TreeNode(lst[i])
                queue.append(current.left)
            i += 1

            # Assign the right child
            if i < len(lst) and lst[i] is not None:
                current.right = TreeNode(lst[i])
                queue.append(current.right)
            i += 1

        return root


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))
        return True

if __name__ == '__main__':
    p = TreeNode.list_to_tree([1, 2])
    q = TreeNode.list_to_tree([1, None, 2])
    t = Solution().isSameTree(p, q)
    print(t)

