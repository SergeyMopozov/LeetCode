"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
"""

class Solution:
    def minStartValue(self, nums) -> int:
        prefix = [nums[0]]
        for n in nums[1:]:
            prefix.append(n+prefix[-1])

        if 1 - min(prefix) < 1:
            return 1
        else:
            return 1 - min(prefix)


sol = Solution()
nums = [-3,2,-3,4,2]
print(sol.minStartValue(nums))

nums = [1, 2]
print(sol.minStartValue(nums))

nums = [1, -2, -3]
print(sol.minStartValue(nums))
