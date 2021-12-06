"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
"""

class Solution:
    def combine(self, n: int, k: int):
        result = []

        def dfs(i, row):
            if len(row) == k:
                result.append(row[:])
                return
            for j in range(i, n):
                row.append(j + 1)
                dfs(j + 1, row)
                row.pop()

        dfs(0, [])
        return result



sol = Solution()
n = 4
k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
print(sol.combine(n, k))

n = 1
k = 1
print(sol.combine(n, k))
