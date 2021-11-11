"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
"""

class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        for i in range(n_rows):
            for j in range(n_cols):
                if i-1 >= 0 and j-1 >= 0:

                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
        return True


sol = Solution()
matrix = [[1, 2, 3, 4],
          [5, 1, 2, 3],
          [9, 5, 1, 2]]
print(sol.isToeplitzMatrix(matrix))

matrix = [[1, 2, 3, 4],
          [5, 1, 1, 3],
          [9, 5, 1, 2]]
print(sol.isToeplitzMatrix(matrix))

matrix = [[1,2],
          [2,2]]

print(sol.isToeplitzMatrix(matrix))