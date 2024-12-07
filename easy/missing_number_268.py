from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = len(nums) + 1
        for i in range(minimum, maximum):
            if i not in nums:
                return i


if __name__ == '__main__':
    t = Solution().missingNumber(nums = [9,6,4,2,3,5,7,0,1])
    print(t)
