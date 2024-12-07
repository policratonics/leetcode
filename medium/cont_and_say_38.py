class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        def counter(res):
            result = []
            count = 1
            for i in range(1, len(res)):
                if res[i] == res[i - 1]:
                    count += 1
                else:
                    result.append(f"{count}{res[i-1]}")
                    count = 1
            result.append(f"{count}{res[-1]}")
            return "".join(result)

        res = "1"
        for i in range(1, n):
            res = counter(res)
        return res


if __name__ == '__main__':
    t = Solution().countAndSay(4)
    print(t)