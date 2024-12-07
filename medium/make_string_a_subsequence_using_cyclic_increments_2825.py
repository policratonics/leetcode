class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
Hint 1
Consider the indices we will increment separately.
Hint 2
We can maintain two pointers: pointer i for str1 and pointer j for str2, while ensuring they remain within the bounds of the strings.
Hint 3
If both str1[i] and str2[j] match, or if incrementing str1[i] matches str2[j], we increase both pointers; otherwise, we increment only pointer i.
Hint 4
It is possible to make str2 a subsequence of str1 if j is at the end of str2, after we can no longer find a match.
        """