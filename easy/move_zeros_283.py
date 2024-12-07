from typing import List


class Solution:
    def move_zero(self, nums: List[int]) -> None:
        not_zero_element = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[not_zero_element] = nums[i]
                not_zero_element += 1
        for i in range(not_zero_element, len(nums)):
            nums[i] = 0


        return nums

if __name__ == '__main__':
    Solution().move_zero([1])
