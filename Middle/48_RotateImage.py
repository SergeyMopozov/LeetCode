"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""


# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         self.transpose(matrix)
#         self.reflect(matrix)
#
#     def transpose(self, matrix):
#         n = len(matrix)
#         for i in range(n):
#             for j in range(i, n):
#                 matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
#
#     def reflect(self, matrix):
#         n = len(matrix)
#         for i in range(n):
#             for j in range(n // 2):
#                 matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def _transpose(matrix):

                n_rows = len(matrix)
                n_cols = len(matrix[0])

                for i in range(n_rows):
                    for j in range(i, n_cols):
                        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        def _reflect(matrix):

                n_rows = len(matrix)
                n_cols = len(matrix[0])
                for i in range(n_rows):
                    left = 0
                    right = n_cols - 1
                    while left < right:
                        matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                        left += 1
                        right -= 1

        _transpose(matrix)
        _reflect(matrix)


sol = Solution()
matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]
# Output: [[15,13,2,5],
#          [14,3,4,1],
#          [12,6,8,9],
#          [16,7,10,11]]
sol.rotate(matrix)
print(matrix)
