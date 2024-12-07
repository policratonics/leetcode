class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        l_h = len(haystack)
        l_n = len(needle)

        for i in range(l_h - l_n + 1):
            if haystack[i:i + l_n] == needle:
                return i
        return -1

if __name__ == '__main__':
    t = Solution().str_str("sadbutsad", "sad")
    print(t)