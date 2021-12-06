"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    pass
                elif i-1 >= 0 and j-1 >= 0:
                    grid[i][j] = min(grid[i][j]+grid[i-1][j], grid[i][j]+grid[i][j-1])
                elif i-1 < 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                else:

                    grid[i][j] = grid[i][j] + grid[i-1][j]

        return grid[m-1][n-1]





sol = Solution()
grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]
print(sol.minPathSum(grid))
