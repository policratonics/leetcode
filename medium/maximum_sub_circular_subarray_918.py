from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def sum_max(arr):
            current_sum = max_sum = arr[0]
            for num in arr[1:]:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum

        def sum_min(arr):
            current_sum = min_sum = arr[0]
            for num in arr[1:]:
                current_sum = min(num, current_sum + num)
                min_sum = min(min_sum, current_sum)
            return min_sum

        total_sum = sum(nums)
        min_sum = sum_min(nums)
        max_sum = sum_max(nums)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)

if __name__ == '__main__':
    t = Solution().maxSubarraySumCircular(nums = [1,-2,3,-2])
    print(t)

