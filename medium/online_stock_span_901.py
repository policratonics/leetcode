import string


class StockSpanner:

    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        span = 1
        while self.prices and self.prices[-1] <= price:
            self.prices.pop()
            span += self.spans.pop()

        self.prices.append(price)
        self.spans.append(span)
        return span


class StockSpanner2:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        st = []
        count = 1
        for i in range(len(self.stack) - 2, - 1, - 1):
            while st and self.stack[st[-1]] <= price:
                st.pop()
            if st:
                count += 1
            st.append(i)
            print(count)
        return count

if __name__ == '__main__':
    #[29],[91],[62],[76],[51]]
    ss = StockSpanner2()
    ss.next(29)
    ss.next(91)
    ss.next(62)
    ss.next(76)
    ss.next(51)

import random

s = "".join(random.choices(string.ascii_lowercase, k=23))