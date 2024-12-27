from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # dp = [0]*len(values)
        # for i in range(len(values)):
        #     for j in range(len(values) - 1, -1, -1):
        #         if i < j:
        #             dp[i] = max(dp[i], values[i] + values[j] + i - j)
        #
        # return max(dp)
        curr  = values[0]
        score = float("-inf")
        for i in range(1, len(values)):
            score = max(score, curr + values[i] - i)
            curr = max(curr, values[i] + i)
        return score


if __name__ == '__main__':
    values = [8, 1, 5, 2, 6]
    # values = [1, 2]
    # values = [1, 3, 5]
    print(Solution().maxScoreSightseeingPair(values))