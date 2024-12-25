from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        mult = 1
        for i in range(n):
            answer[i] = mult
            mult *= nums[i]
        mult = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= mult
            mult *= nums[i]
        return answer


if __name__ == '__main__':
    t = Solution().productExceptSelf(nums = [1,2,3,4])
    print(t)