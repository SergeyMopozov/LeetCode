"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique
if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations
for the given input.
"""

class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def _dfs(idx, current, total):
            if total == target:
                result.append(current.copy())
                return
            if idx >= len(candidates) or total > target:
                return

            current.append(candidates[idx])
            _dfs(idx, current, total+candidates[idx])
            current.pop()
            _dfs(idx+1, current, total)

        _dfs(0, [], 0)

        return result


sol = Solution()
candidates = [2,3,6,7]
target = 7
#Output: [[2,2,3],[7]]
print(sol.combinationSum(candidates, target))

candidates = [2,3,5]
target = 8
#Output: [[2,2,2,2],[2,3,3],[3,5]]
print(sol.combinationSum(candidates, target))
