from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # rows, cols = len(grid), len(grid[0])
        # dp = [[0] * cols for _ in range(rows)]
        # for i in range(rows):
        #     for j in range(cols):
        #         if i == 0 and j == 0:
        #             dp[i][j] = grid[i][j]
        #         elif i == 0:
        #             dp[i][j] = dp[i][j - 1] + grid[i][j]
        #         elif j == 0:
        #             dp[i][j] = dp[i - 1][j] + grid[i][j]
        #         else:
        #             dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        #
        # return dp[-1][-1]
        ROWS, COLS = len(grid), len(grid[0])
        dp = [float("inf")] * (COLS + 1)
        dp[COLS - 1] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                a = grid[r][c] + min(dp[c], dp[c + 1])
                dp[c] = a

        return dp[0]

if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))

