import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []
        total_ratio = 0
        def calc_gain(i):
            return ((classes[i][0]+1)/(classes[i][1]+1) - (classes[i][0]/classes[i][1]))

        for i, class_ in enumerate(classes):
            gain = calc_gain(i)
            heapq.heappush(max_heap, (-gain, i))
        for _ in range(extraStudents):
            _, i = heapq.heappop(max_heap)
            classes[i][0] += 1
            classes[i][1] += 1
            gain = calc_gain(i)
            heapq.heappush(max_heap, (-gain,i))
        while max_heap:
            gain, i = heapq.heappop(max_heap)
            total_ratio += classes[i][0]/classes[i][1]
        return total_ratio/len(classes)


# class Solution:
#     def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
#         h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in classes]
#         heapify(h)
#         for _ in range(extraStudents):
#             _, a, b = heappop(h)
#             a, b = a + 1, b + 1
#             heappush(h, (a / b - (a + 1) / (b + 1), a, b))
#         return sum(v[1] / v[2] for v in h) / len(classes)


if __name__ == '__main__':
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents = 4
    print(Solution().maxAverageRatio(classes, extraStudents))