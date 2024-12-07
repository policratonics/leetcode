from typing import List


class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if num1[p1] > num2[p2]:
                num1[p] = num1[p1]
                p1 -= 1
            else:
                num1[p] = num2[p2]
                p2 -= 1
            p -= 1
        num1[:p2 + 1] = num2[:p2 + 1]

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    Solution().merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]