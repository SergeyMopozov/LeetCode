"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers

"""

class Solution:
    def generate(self, numRows: int):

        def get_row(prev_row):
            new_row = []
            for j in range(len(prev_row)+1):
                if j == 0:
                    new_row.append(0+prev_row[j])
                elif j == len(prev_row):
                    new_row.append(0 + prev_row[j-1])
                else:
                    new_row.append(prev_row[j-1] + prev_row[j])
            return new_row
        triangle = [[1], [1, 1]]

        for i in range(2, numRows):
            triangle.append(get_row(triangle[i-1]))

        return triangle[:numRows]

    def getRow(self, rowIndex):
        def get_row(prev_row):
            new_row = []
            for j in range(len(prev_row)+1):
                if j == 0:
                    new_row.append(0+prev_row[j])
                elif j == len(prev_row):
                    new_row.append(0 + prev_row[j-1])
                else:
                    new_row.append(prev_row[j-1] + prev_row[j])
            return new_row
        triangle = [[1], [1, 1]]

        for i in range(2, rowIndex+1):
            triangle.append(get_row(triangle[i-1]))

        return triangle[rowIndex]

sol = Solution()
n = 5
#  [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(sol.generate(n))
print(sol.getRow(n))