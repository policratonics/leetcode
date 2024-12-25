from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_kills = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(row, col, dr, dc):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "W":
                return 0
            count = 1 if grid[row][col] == "E" else 0
            return count + dfs(row + dr, col + dc, dr, dc)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    all_kills = 0
                    for dr, dc in dirs:
                        all_kills += dfs(row, col, dr, dc)
                    max_kills = max(max_kills, all_kills)
        return max_kills



        # d = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        #
        # def find_enemy(row, col):
        #     # Base cases
        #     if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):  # Check boundaries
        #         return 0
        #     enemy_count = 1 if grid[row][col] == "E" else 0  # Count if enemy present
        #
        #     # Directions: up, down, left, right
        #     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        #
        #     # Recursive calls in all directions
        #     for dx, dy in directions:
        #         enemy_count += find_enemy(row + dx, col + dy)
        #
        #     return enemy_count
        #
        # max_kills = 0
        # all_kills = 0
        #
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == "0":
        #             all_kills += find_enemy(row, col)
        #             max_kills = max(max_kills, all_kills)
        # return max_kills


if __name__ == '__main__':
    t = Solution().maxKilledEnemies(grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]])
    print(t)

    # enemy_count = 0
    # while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
    #     if grid[row][col] == "W":
    #         break
    #     if grid[row][col] == "E":
    #         enemy_count += 1
    #     row, col = row + d[0], col + d[1]
    # return enemy_count
