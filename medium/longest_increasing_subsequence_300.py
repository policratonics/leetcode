from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [0]*n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[j] + 1, lis[i])
        return max(lis) + 1


if __name__ == '__main__':
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [0,1,0,3,2,3]
    nums = [7,7,7,7,7,7,7]
    sol = Solution().lengthOfLIS(nums)
    assert sol == 4