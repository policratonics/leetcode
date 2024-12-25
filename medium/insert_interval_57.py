from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort(key=lambda x: x[0])
            res = [intervals[0]]
            for i in range(1, len(intervals)):
                last = res[-1]
                curr = intervals[i]
                if last[1] >= curr[0]:
                    last[1] = max(last[1], curr[1])
                else:
                    res.append(curr)
            return res

        intervals.append(newInterval)
        return merge(intervals)


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(Solution().insert(intervals, newInterval))