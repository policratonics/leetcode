from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        if not nums:
            return nums
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        nums[:] = nums[:slow]
        return slow

if __name__ == '__main__':
    t = Solution().remove_element(nums=[3, 2, 2, 3], val=3)
    print(t)