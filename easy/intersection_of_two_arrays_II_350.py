from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = defaultdict(int)
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        for num in nums1:
            map[num] += 1
        result = []
        for num in nums2:
            if num in map.keys() and map[num] > 0:
                result.append(num)
                map[num] -= 1
        return result


if __name__ == '__main__':
    # t = Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
    t = Solution().intersect(nums1 = [3,1,2], nums2 =[1,1])
    print(t)