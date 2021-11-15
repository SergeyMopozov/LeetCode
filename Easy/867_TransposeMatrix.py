"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
"""

class Solution:
    def transpose(self, matrix):
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        result = []
        for i in range(n_cols):
            row = []
            for j in range(n_rows):
                row.append(matrix[j][i])
                #matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            result.append(row)
        return result


sol = Solution()
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(sol.transpose(matrix))

matrix = [[1, 2, 3],
          [4, 5, 6]]
print(sol.transpose(matrix))
