from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        storage = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in storage.keys():
                if abs(i - storage[nums[i]]) <= k:
                    return True
            storage[nums[i]] = i
        return False

if __name__ == '__main__':
    t = Solution().containsNearbyDuplicate(nums = [1,0,1,1], k = 1)
    print(t)