class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        last = self.queue[0]
        temp = self.queue[1:]
        self.queue, temp = temp, self.queue
        return last

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if self.queue:
            return False
        return True