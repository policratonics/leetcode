from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        next = 1
        initial_len = len(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[next] = nums[i]
                next += 1
        return next, len(nums), nums

if __name__ == '__main__':
    t = Solution().removeDuplicates(nums=[1, 1, 2])
    print(t)