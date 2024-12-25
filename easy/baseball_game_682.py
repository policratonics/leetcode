from math import prod
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i.isdigit() or i.lstrip('-').isdigit():
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i == "D":
                record = stack[-1] * 2
                stack.append(record)
            elif i == "+":
                record = stack[-1] + stack[-2]
                stack.append(record)
                prod()

        return sum(stack)


if __name__ == '__main__':
    t = Solution().calPoints(["5","-2","4","C","D","9","+","+"])
    assert t == 27