from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_container = 0
        while left < right:
            current_container = min(height[left], height[right]) * (right - left)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

            max_container = max(max_container, current_container)
        return max_container


if __name__ == '__main__':
    t = Solution().maxArea(height = [1,8,6,2,5,4,8,3,7])
    print(t)