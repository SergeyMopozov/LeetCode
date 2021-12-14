"""
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
"""

#from collections import Counter


class Solution:
    def permuteUnique(self, nums):
        # curr = []
        # result = set()
        # n = len(nums)
        #
        # available = [1] * n
        #
        # def _dfs():
        #     if len(curr) == n:
        #         result.add(tuple(curr.copy()))
        #         return
        #     for i in range(n):
        #         if available[i] == 1:
        #             curr.append(nums[i])
        #             available[i] = 0
        #             _dfs()
        #
        #             available[i] = 1
        #             curr.pop()
        #
        # _dfs()
        # return [list(r) for r in result]

        result = []
        n = len(nums)

        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        #print(counter)
        def _dfs(curr, counter):
            if len(curr) == n:
                result.append(curr.copy())
                return
            for i in counter:
                if counter[i] >= 1:
                    curr.append(i)
                    counter[i] -= 1
                    _dfs(curr, counter)

                    curr.pop()
                    counter[i] += 1

        _dfs([], counter)
        return result


sol = Solution()
nums = [1,1,2]

# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
print(sol.permuteUnique(nums))


nums = [1, 2, 3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(sol.permuteUnique(nums))
