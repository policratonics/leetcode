class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        operations = {
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }
        stack, sign, value = [], "+", 0
        for i, char in enumerate(s):
            if char.isdigit():
                value = value * 10 + int(char)
            if i == len(s) - 1 or char in "+-*/":
                if sign == "+":
                    stack.append(value)
                elif sign == "-":
                    stack.append(-value)
                elif sign in "*/":
                    stack[-1] = operations.get(sign)(stack[-1], value)
                value = 0
                sign = char
        return sum(stack)


if __name__ == '__main__':
    t = Solution().calculate("0-42")
    print(t)