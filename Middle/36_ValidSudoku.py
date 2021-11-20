"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
"""
algorithm:
1. Count numbers by rows
2. Count numbers by cols
3. Count numbers by box
if duplicated return false 
"""
class Solution:
    def isValidSudoku(self, board) -> bool:

        for row in board:
            row_count = {}
            for r in row:
                if r != '.':
                    if r not in row_count:
                        row_count[r] = 0
                    row_count[r] += 1
                    if row_count[r] >= 2:
                        return False

        for i in range(len(board[0])):
            col_count = {}
            for j in range(len(board)):
                if board[j][i] != '.':
                    if board[j][i] not in col_count:
                        col_count[board[j][i]] = 0
                    col_count[board[j][i]] += 1
                    if col_count[board[j][i]] >= 2:
                        return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                box_count = {}
                for a in range(3):
                    for b in range(3):
                        if board[i+a][j+b] != '.':
                            if board[i+a][j+b] not in box_count:
                                box_count[board[i+a][j+b]] = 0
                            box_count[board[i+a][j+b]] += 1
                            if box_count[board[i+a][j+b]] >= 2:
                                return False

        return True


sol = Solution()
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))

