"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
"""

class Solution:
    def findDiagonalOrder(self, mat):

        result = []
        rows = len(mat)
        cols = len(mat[0])

        for n in range(rows + cols - 1):

            if (n >= rows) and n % 2 == 0:
                j += 2
                i = n - j
            elif (n >= cols) and n % 2 != 0:
                i += 2
                j = n - i
            elif n % 2 == 0:
                i = n
                j = 0
            else:
                i = 0
                j = n
            #print(i, j)
            while (0 <= i < rows) and (0 <= j < cols) and i + j <= n:
                #print(i, j, end=' ')
                result.append(mat[i][j])
                if n % 2 == 0:
                    j += 1
                    i = n - j
                else:
                    i += 1
                    j = n - i
            #print(i, j)
        return result

sol = Solution()
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
#Output: [1,2,4,7,5,3,6,8,9]
print(sol.findDiagonalOrder(mat))
#
#
# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9],
#        [10,11,12]]
# #Output: [1,2,4,7,5,3,6,8,9,10,11,12]
# print(sol.findDiagonalOrder(mat))
#
#
# mat = [[1,2,3,4],
#        [5,6,7,8],
#        [9,10,11,12]]
# #Output: [1,2,4,7,5,3,6,8,9,10,11,12]
# print(sol.findDiagonalOrder(mat))

mat = [[2,3]]
print(sol.findDiagonalOrder(mat))

mat = [[2],[3]]
print(sol.findDiagonalOrder(mat))

