import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(value, index) for index, value in enumerate(nums)]
        heap.sort(key=lambda x: [x[0]])
        res = [0] * len(nums)
        while k > 0:
            value, index = heapq.heappop(heap)
            heapq.heappush(heap, (value*multiplier, index))
            k -= 1

        for v, i in heap:
            res[i] = v
        return res

# [8,4,6,5,6]
if __name__ == '__main__':
    # nums = [2, 1, 3, 5, 6]
    nums = [2, 1]
    # k = 5
    k = 1
    multiplier = 2
    # multiplier = 2
    print(Solution().getFinalState(nums, k, multiplier))