from typing import List


class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     count = [0, 0, 0]
    #
    #     for num in nums:
    #         count[num] += 1
    #
    #     index = 0
    #     for color in range(3):
    #         for _ in range(count[color]):
    #             nums[index] = color
    #             index += 1

    # def sortColors(self, nums: List[int]) -> None:
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(0, n-i-1):
    #             if nums[j] > nums[j+1]:
    #                 nums[j], nums[j+1] = nums[j+1], nums[j]

    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag Algorithm
        """
        n = len(nums)
        low, mid, high = 0, 0, n-1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1