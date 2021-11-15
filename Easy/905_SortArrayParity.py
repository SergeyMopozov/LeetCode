"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""

class Solution:
    def sortArrayByParity(self, nums):
        odd = []
        even = []

        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        return even + odd


sol = Solution()
nums = [3,1,2,4]
print(sol.sortArrayByParity(nums))