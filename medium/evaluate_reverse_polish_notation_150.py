from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operations = {
            "+": lambda x,y : x + y,
            "-": lambda x,y : x - y,
            "*": lambda x,y : x * y,
            "/": lambda x,y : int(x / y),
        }
        for i, val in enumerate(tokens):
            if val.lstrip('-').isdigit():
                stack.append(val)
            elif val in "+-*/":
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                temp = operations.get(val)(operand_1, operand_2)
                stack.append(temp)
        return sum(stack)


if __name__ == '__main__':
    t = Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    # t = Solution().evalRPN(["4","3","-"])
    print(t)


