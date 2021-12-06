"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #
        # def _recurse(i, j):
        #     if i == m-1:
        #         return 1
        #     if j == n-1:
        #         return 1
        #     return _recurse(i, j+1) + _recurse(i+1, j)
        #
        # return _recurse(0, 0)

        dp = [[0] * n for i in range(m)]
        print(dp)
        for i in range(m):
            dp[i][0] = 1
        #print(dp)
        for i in range(n):
            dp[0][i] = 1
        #print(dp)

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        #print(dp)

        return dp[m-1][n-1]


sol = Solution()
m = 7
n = 3
print(sol.uniquePaths(m, n))
