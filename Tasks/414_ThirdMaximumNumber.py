"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.
"""
class Solution:
    def thirdMax(self, nums) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')

        for n in set(nums):
            if n > first:
                third = second
                second = first
                first = n
            elif n > second:
                third = second
                second = n
            elif n > third:
                third = n

        if third == float('-inf'):
            return first
        else:
            return third


sol = Solution()
n_arr = [1, 2, 2, 4]
print(sol.thirdMax(n_arr))
