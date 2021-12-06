"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        zeros = {'row': set(), 'col': set()}

        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == 0:
                    zeros['row'].add(i)
                    zeros['col'].add(j)

        for i in range(n_rows):
            for j in range(n_cols):
                if i in zeros['row'] or j in zeros['col']:
                    matrix[i][j] = 0


sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
#Output: [[1,0,1],[0,0,0],[1,0,1]]
sol.setZeroes(matrix)
print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
sol.setZeroes(matrix)
print(matrix)
