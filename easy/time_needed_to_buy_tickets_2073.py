from collections import deque
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # total_time = 0
        # for i in range(len(tickets)):
        #     # For people before or at k, consider their full ticket count or tickets[k]
        #     if i <= k:
        #         total_time += min(tickets[i], tickets[k])
        #     # For people after k, consider their ticket count or tockens[k] - 1.
        #     else:
        #         total_time += min(tickets[i], tickets[k] - 1)
        # return total_time

        queue = deque([(tickets[i], i) for i in range(len(tickets))])
        time = 0
        while queue:
            tickets_left, person = queue.popleft()
            time += 1
            if tickets_left > 1:
                queue.append((tickets_left - 1, person))
            if person == k and tickets_left == 1:
                return time


if __name__ == '__main__':
    t = Solution().timeRequiredToBuy(tickets = [2,3,2], k = 2)
    print(t)