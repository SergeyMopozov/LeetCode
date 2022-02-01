"""
You are given an m x n matrix M initialized with all 0's and an array of operations ops,
where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.
"""


class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        # mat = [[0]*n for _ in range(m)]
        #
        # for a, b in ops:
        #     for i in range(a):
        #         for j in range(b):
        #             mat[i][j] += 1
        #
        # flat = []
        # for i in range(m):
        #     flat += mat[i]
        #
        # max_mat = max(flat)
        # max_count = 0
        # for n in flat:
        #     if n == max_mat:
        #         max_count += 1
        #
        # return max_count

        # if len(ops) == 0:
        #     return m * n

        x = m
        y = n
        for a, b in ops:
            x = min(x, a)
            y = min(y, b)

        return x*y


sol = Solution()
m = 3
n = 3
ops = [[2, 2], [3, 3]]
print(sol.maxCount(m, n, ops))

m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
print(sol.maxCount(m, n, ops))

m = 3
n = 3
ops = []
print(sol.maxCount(m, n, ops))
