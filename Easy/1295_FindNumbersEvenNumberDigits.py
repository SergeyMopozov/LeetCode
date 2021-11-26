"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""

class Solution:
    def findNumbers(self, nums):
        counter = 0
        for n in nums:
            res = n
            d_counter = 0
            while res != 0:
                res = res // 10
                d_counter += 1

            if d_counter % 2 == 0:
                counter += 1

        return counter


sol = Solution()
nums = [12, 345, 2, 6, 7896]
print(sol.findNumbers(nums))
