"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""



class Solution:
    def subsetsWithDup(self, nums):

        def backtrack(first, curr, k, counter):
            # if the combination is done
            if len(curr) == k:
                output.add(tuple(sorted(curr)))
                return
            for i in range(first, n):
                if counter[nums[i]] >= 1:
                    # add nums[i] into the current combination
                    curr.append(nums[i])
                    counter[nums[i]] -= 1
                    # use next integers to complete the combination
                    backtrack(i + 1, curr, k, counter)
                    # backtrack
                    curr.pop()
                    counter[nums[i]] += 1

        output = set()
        n = len(nums)

        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1

        for k in range(len(nums) + 1):
            backtrack(0, [], k, counter)
        return sorted([list(r) for r in output])


sol = Solution()
nums = [1, 2, 2]
# [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(sol.subsetsWithDup(nums))


nums = [1, 1, 2]
# [[],[1],[1,1],[1,1,2],[2],[1,2]]
print(sol.subsetsWithDup(nums))
