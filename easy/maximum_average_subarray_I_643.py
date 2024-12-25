from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = window_sum = start = 0
        for i in range(len(nums)):
            window_sum += nums[i]
            if (i - start + 1) == k:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[start]
                start += 1

        return max_sum/k


if __name__ == '__main__':
    nums = [-1]
    k = 1
    print(Solution)