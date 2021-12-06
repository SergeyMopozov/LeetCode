"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""
class Solution:
    def generateMatrix(self, n: int):

        result = [[0 for i in range(n)] for j in range(n)]
        left = 0
        right = n-1
        up = 0
        down = n-1

        cur_row = 0
        cur_col = 0
        horizon = True
        vertical = False
        forward = True
        backward = False
        i = 1
        while i <= n*n:

            if horizon and forward:
                if cur_col <= right:
                    result[cur_row][cur_col] = i
                    i += 1
                    cur_col += 1
                else:
                    horizon = False
                    vertical = True
                    cur_row += 1
                    cur_col -= 1
                    up += 1

            elif vertical and forward:
                if cur_row <= down:
                    result[cur_row][cur_col] = i
                    i += 1
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
                    result[cur_row][cur_col] = i
                    i += 1
                    cur_col -= 1
                else:
                    horizon = False
                    vertical = True
                    cur_row -= 1
                    cur_col += 1
                    down -= 1

            elif vertical and backward:
                if cur_row >= up:
                    result[cur_row][cur_col] = i
                    i += 1
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
n = 1
print(sol.generateMatrix(n))

n = 2
print(sol.generateMatrix(n))

n = 3
print(sol.generateMatrix(n))

n = 4
print(sol.generateMatrix(n))
