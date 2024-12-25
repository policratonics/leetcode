from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            if row < 0 or row >=rows or col < 0 or col >= cols or grid[row][col] == "0":
                return True
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands

    def numIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque([r,c])
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands