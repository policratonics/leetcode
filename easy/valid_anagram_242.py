from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        if len(s) != len(t):
            return False
        for char in t:
            if s1[char]:
                s1[char] -= 1
        if sum(s1.values()) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    t = Solution().isAnagram( s = "anagram", t = "nagaram")
    print(t)