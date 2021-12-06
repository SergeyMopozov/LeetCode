"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # all = []
        # for m in matrix:
        #     all += m
        # all = set(all)
        # if target in all:
        #     return True
        # else:
        #     return False

        # n_rows = len(matrix)
        # n_cols = len(matrix[0])
        # left = 0
        # right = n_cols - 1
        # up = 0
        # down = n_rows - 1
        #
        # while left <= right or up <= down:
        #
        #     middle_h = (left + right) // 2
        #     middle_v = (up + down) // 2
        #     print(middle_v, middle_h)
        #     if matrix[middle_v][middle_h] == target:
        #         return True
        #     elif target < matrix[middle_v][middle_h]:
        #         right = middle_h-1
        #         down = middle_v-1
        #
        #     else:
        #         left = middle_h+1
        #         up = middle_v+1
        #
        # return False

        n_rows = len(matrix)
        n_cols = len(matrix[0])
        low = 0
        high = n_rows * n_cols - 1

        if target < matrix[0][0] or target > matrix[n_rows-1][n_cols-1]:
            return False


        while low <= high:
            middle = (high + low) // 2
            if n_cols == 1:
                i = middle
            elif n_rows == 0:
                i = 0
            else:
                i = middle // n_cols

            if n_rows == 1:
                j = middle
            elif n_cols == 1:
                j = 0
            else:
                j = middle % n_cols
            #print(middle, i, j)
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                high = middle - 1
            else:
                low = middle + 1
        return False


sol = Solution()
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix,  target))

matrix = [[1,2]]
target = 3
print(sol.searchMatrix(matrix,  target))

matrix = [[1]]
target = 1
print(sol.searchMatrix(matrix,  target))

matrix = [[1],
          [3]]
target = 3
print(sol.searchMatrix(matrix,  target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 7
print(sol.searchMatrix(matrix,  target))
