class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        left, right = 0, len(s) - 1
        ls = list(s)
        while left < right:
            if ls[left].lower() in vowels and ls[right].lower() in vowels:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1
            elif ls[left].lower() in vowels and ls[right].lower() not in vowels:
                right -= 1
            else:
                left += 1
        return "".join(ls)


if __name__ == '__main__':
    t = Solution().reverseVowels(s="IceCreAm")
    print(t)