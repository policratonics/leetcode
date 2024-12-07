from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1_idx[val]
                res[idx] = cur
            if cur in nums1_idx:
                stack.append(cur)

        return res


if __name__ == '__main__':
    t = Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
    print(t)