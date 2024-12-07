from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            n = numbers[l] + numbers[r]
            if n < target:
                l += 1
            elif n > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        # for i in range(len(numbers)):
        #     left, right = i+1, len(numbers) - 1
        #     complement = target - numbers[i]
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if numbers[mid] == complement:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] < complement:
        #             left = mid + 1
        #         else:
        #             right = mid - 1


if __name__ == '__main__':
    t = Solution().twoSum(numbers = [2,3,4], target = 6)
    print(t)