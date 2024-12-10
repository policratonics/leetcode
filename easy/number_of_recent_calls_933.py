from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()
        print(len(self.queue))
        return len(self.queue)


if __name__ == '__main__':
    rc = RecentCounter()
    rc.ping(1)
    rc.ping(100)
    rc.ping(3001)
    rc.ping(3002)