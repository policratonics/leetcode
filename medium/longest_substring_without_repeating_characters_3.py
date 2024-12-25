class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_set = set()
        result = i = 0
        for index, char in enumerate(s):
            while ch_set and char in ch_set:
                ch_set.remove(char)
                i += 1
            ch_set.add(char)
            result = max(result, index - i + 1)
        return result


if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))