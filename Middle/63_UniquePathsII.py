"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        n_rows = len(obstacleGrid)
        n_cols = len(obstacleGrid[0])
        if obstacleGrid[n_rows - 1][n_cols - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for i in range(n_cols)] for j in range(n_rows)]
        # print(dp)
        dp[0][0] = 1
        for i in range(1, n_rows):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0


        # print(dp)
        for i in range(1, n_cols):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0
        #print(dp)

        for i in range(1, n_rows):
            for j in range(1, n_cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        #print(dp)

        return dp[n_rows - 1][n_cols - 1]



sol = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
#Output: 2
print(sol.uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,1],[0,0]]
#Output: 1
print(sol.uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,0,0,0,0],
                [0,0,0,0,1],
                [0,0,0,1,0],
                [0,0,1,0,0]]
print(sol.uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],
                [1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],
                [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],
                [0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],
                [1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],
                [0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
                [0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
                [0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
                [0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
                [1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
                [0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],
                [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],
                [0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
                [0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],
                [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],
                [1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],
                [1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
print(sol.uniquePathsWithObstacles(obstacleGrid))
