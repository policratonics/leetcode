from collections import Counter, deque


class Solution():
    def first_unique_char(self, s: str) -> int:
        # we can use the Counter from collections
        # like frequencies = Counter(s)
        # or a loop to fill a frequencies dictionary
        # or defaultdict(int)
        frequencies = {}
        for char in s:
            frequencies[char] = frequencies.get(char, 0) + 1

        # define a queue
        queue = deque()
        for index, char in enumerate(s):
            if frequencies[char] == 1:
                queue.append((char, index))

        while queue:
            char, index = queue[0]
            if frequencies[char] == 1:
                return index
            queue.popleft()
        return -1
