"""
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column
and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting
from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
"""


class Solution:
    def diagonalSort(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        diag = {}

        for i in range(rows):
            for j in range(cols):
                if i-j not in diag:
                    diag[i-j] = []
                diag[i - j].append(mat[i][j])

        for d in diag:
            #diag[d] = sorted(diag[d])
            diag[d].sort()

        for i in range(rows):
            for j in range(cols):
                mat[i][j] = diag[i-j].pop(0)

        return mat




sol = Solution()

mat = [[3,3,1,1],
       [2,2,1,2],
       [1,1,1,2]]
#Output: [[1,1,1,1],
#         [1,2,2,2],
#         [1,2,3,3]]

print(sol.diagonalSort(mat))
