class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        top = self.stack[::-1][0]
        temp = self.stack[::-1][1:]
        self.stack = temp[::-1]
        return top

    def top(self) -> int:
        return self.stack[::-1][0]

    def empty(self) -> bool:
        if self.stack:
            return False
        return True

# Your MyStack object will be instantiated and called as such:
if __name__ == '__main__':

    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    print(obj)