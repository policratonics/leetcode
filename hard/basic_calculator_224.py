class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        def calc(s: str, index: int) -> (int, int):
            current_result = 0
            sign = 1
            i = index

            while i < len(s):
                char = s[i]
                if char.isdigit():
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    current_result += sign * num
                    i -= 1
                if char == "+":
                    sign = 1
                elif char == "-":
                    sign = -1
                elif char == "(":
                    sub_result, new_index = calc(s, i + 1)
                    current_result += sign * sub_result
                    i = new_index
                elif char == ")":
                    return current_result, i
                i += 1
            return current_result, i

        result, _ = calc(s, 0)
        return result



if __name__ == '__main__':
    t = Solution().calculate("(1+(4+5+2)-3)+(6+8)")
    print(t)