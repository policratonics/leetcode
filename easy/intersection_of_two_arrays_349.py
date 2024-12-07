from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        left = 0
        right = 0

        result = set()

        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                result.add(nums1[left])
                left += 1
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        return list(result)

        # result = []
        # set1 = set(nums1)
        # set2 = set(nums2)
        # for i in set1:
        #     if i in set2:
        #         result.append(i)
        # return result


        # nums1_set = set(nums1)
        # nums2_set = set(nums2)
        # return list(nums1_set.intersection(nums2_set))


if __name__ == '__main__':
    t = Solution().intersection(nums1 = [1, 2], nums2 = [1, 1])
    print(t)