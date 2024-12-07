from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        for num in nums:
            if num == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return len(nums) - l
        # left = 0  # Start of the window
        # longest = 0
        # zeros = 0  # Count of zeros in the window
        #
        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         zeros += 1
        #
        #     # When zeros exceed k, shrink the window by moving the left pointer
        #     while zeros > k:
        #         if nums[left] == 0:
        #             zeros -= 1
        #         left += 1
        #
        #     # Update the maximum length of the window
        #     longest = max(longest, right - left + 1)
        #
        # return longest

if __name__ == '__main__':
    Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)