from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        suplement = defaultdict(None)
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in suplement.keys():
                return [suplement[nums[i]], i]
            suplement[diff] = i




if __name__ == '__main__':
    t = Solution().twoSum(nums = [3,2,4], target = 6)
    print(t)