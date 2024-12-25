from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            last = res[-1]
            curr = intervals[i]
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                res.append(curr)
        return res

if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))