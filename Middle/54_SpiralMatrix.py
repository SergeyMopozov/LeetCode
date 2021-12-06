"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

class Solution:
    def spiralOrder(self, matrix):
        result = []
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = cols-1
        up = 0
        down = rows-1

        cur_row = 0
        cur_col = 0
        horizon = True
        vertical = False
        forward = True
        backward = False

        while len(result) < cols*rows:

            if horizon and forward:
                if cur_col <= right:
                    result.append(matrix[cur_row][cur_col])
                    cur_col += 1
                else:
                    horizon = False
                    vertical = True
                    cur_row += 1
                    cur_col -= 1
                    up += 1
            elif vertical and forward:
                if cur_row <= down:
                    result.append(matrix[cur_row][cur_col])
                    cur_row += 1
                else:
                    horizon = True
                    vertical = False
                    forward = False
                    backward = True
                    cur_row -= 1
                    cur_col -= 1
                    right -= 1
            elif horizon and backward:
                if cur_col >= left:
                    result.append(matrix[cur_row][cur_col])
                    cur_col -= 1
                else:
                    horizon = False
                    vertical = True
                    cur_row -= 1
                    cur_col += 1
                    down -= 1
            elif vertical and backward:
                if cur_row >= up:
                    result.append(matrix[cur_row][cur_col])
                    cur_row -= 1
                else:
                    horizon = True
                    vertical = False
                    forward = True
                    backward = False
                    cur_row += 1
                    cur_col += 1
                    left += 1

        return result


sol = Solution()

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]
print(sol.spiralOrder(matrix))


matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
print(sol.spiralOrder(matrix))


matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
#Output: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
print(sol.spiralOrder(matrix))


matrix = [[1,2,3,4]]
#Output: [1,2,3,4,]
print(sol.spiralOrder(matrix))
matrix = [[1],
          [2],
          [3],
          [4]]
#Output: [1,2,3,4,]
print(sol.spiralOrder(matrix))
