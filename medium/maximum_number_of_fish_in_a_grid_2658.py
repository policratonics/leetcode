from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_fish = 0
        visited = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r,c) in visited:
                return 0
            fish = grid[r][c]
            # grid[r][c] = 0
            visited.add((r, c))
            return sum([dfs(r + 1, c),
            dfs(r, c + 1),
            dfs(r - 1, c),
            dfs(r, c - 1)]) + fish

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    max_fish = max(max_fish, dfs(r, c))
        return max_fish


if __name__ == '__main__':
    # grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
    t = Solution().findMaxFish(grid)
    print(t)