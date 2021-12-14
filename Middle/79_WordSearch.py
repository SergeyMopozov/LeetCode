"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
class Solution:
    def exist(self, board, word) -> bool:
        EXIST = []
        n_rows = len(board)
        n_cols = len(board[0])
        w_len = len(word)

        def _backtrack(i, j, curr, used, pos):
            #print(''.join(curr))
            if ''.join(curr) == word:
                EXIST.append(1)

            # up
            if pos < w_len and i-1 >= 0 and board[i-1][j] == word[pos] and (i-1, j) not in used:
                curr.append(board[i-1][j])
                used.append((i-1, j))
                pos += 1
                _backtrack(i-1, j, curr, used, pos)
                curr.pop()
                used.pop()
                pos -= 1
            # down
            if pos < w_len and i+1 < n_rows and board[i+1][j] == word[pos] and (i+1, j) not in used:
                curr.append(board[i+1][j])
                used.append((i+1, j))
                pos += 1
                _backtrack(i+1, j, curr, used, pos)
                curr.pop()
                used.pop()
                pos -= 1
            # left
            if pos < w_len and j-1 >= 0 and board[i][j-1] == word[pos] and (i, j-1) not in used:
                curr.append(board[i][j-1])
                used.append((i, j-1))
                pos += 1
                _backtrack(i, j-1, curr, used, pos)
                curr.pop()
                used.pop()
                pos -= 1
            # right
            if pos < w_len and j+1 < n_cols and board[i][j+1] == word[pos] and (i, j+1) not in used:
                curr.append(board[i][j+1])
                used.append((i, j+1))
                pos += 1
                _backtrack(i, j+1, curr, used, pos)
                curr.pop()
                used.pop()
                pos -= 1


        # start exploration on each cell
        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j] == word[0]:
                    _backtrack(i, j, [board[i][j]], [(i, j)], 1)

        if sum(EXIST) > 0:
            return True
        else:
            return False




sol = Solution()
# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]
# word = "ABCCED"
# #Output: true
# print(sol.exist(board, word))
#
#
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"
#
# print(sol.exist(board, word))
#
#
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"
# #Output: false
#
# print(sol.exist(board, word))

board = [["a","b"]]
word = 'ba'

print(sol.exist(board, word))