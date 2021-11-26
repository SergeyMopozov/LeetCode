"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

class Solution:
    def combinationSum2(self, candidates, target: int):

        result = []

        def _dfs(idx, current, total, pool):
            if total == target:
                result.append(current.copy())
                return
            if idx >= len(pool) or total > target:
                return

            # add candidate for combination
            current.append(pool[idx])
            # copy pool of next cadidates
            p = pool.copy()
            # pop already used element
            p.pop(idx)
            _dfs(idx, current, total + pool[idx], p)

            # start
            current.pop()
            p = pool.copy()
            _dfs(idx + 1, current, total, p)

        _dfs(0, [], 0, candidates.copy())

        res_dict = {}
        unique = []
        for r in result:
            if tuple(set(r)) not in res_dict:
                res_dict[tuple(set(r))] = 1
                unique.append(r)

        return unique


sol = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
print(sol.combinationSum2(candidates, target))

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27
print(len(candidates))
#print(sol.combinationSum2(candidates, target))
