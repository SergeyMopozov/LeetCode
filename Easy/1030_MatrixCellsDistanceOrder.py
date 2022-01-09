"""
You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are
on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter)
from the smallest distance to the largest distance. You may return the answer
in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
"""

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int):

        result = []
        for i in range(rows):
            for j in range(cols):
                result.append([i, j])

        return sorted(result, key=lambda x: abs(x[0]-rCenter)+abs(x[1]-cCenter))

sol = Solution()

rows = 1
cols = 2
rCenter = 0
cCenter = 0
#Output: [[0,0],[0,1]]
print(sol.allCellsDistOrder(rows, cols, rCenter, cCenter))

rows = 2
cols = 2
rCenter = 0
cCenter = 1
#Output: [[0,1],[0,0],[1,1],[1,0]]
print(sol.allCellsDistOrder(rows, cols, rCenter, cCenter))

rows = 2
cols = 3
rCenter = 1
cCenter = 2
#[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
#[[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
print(sol.allCellsDistOrder(rows, cols, rCenter, cCenter))


