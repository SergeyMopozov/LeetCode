"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land
and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.
"""

class Solution:
    def islandPerimeter(self, grid) -> int:

        cells = 0
        intersection = 0
        n_rows = len(grid)
        n_cols = len(grid[0])

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    cells += 1
                    if i != 0 and grid[i-1][j] == 1:
                        intersection += 1
                    if j != 0 and grid[i][j-1] == 1:
                        intersection += 1

        return cells * 4 - 2 * intersection



sol = Solution()
grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
#Output: 16
print(sol.islandPerimeter(grid))

grid = [[1]]
#Output: 4
print(sol.islandPerimeter(grid))

grid = [[1, 0]]
#Output: 4
print(sol.islandPerimeter(grid))
