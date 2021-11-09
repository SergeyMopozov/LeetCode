"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums) -> int:
        # O(n) time, O(n) space
        # ndict = {}
        #
        # for n in nums:
        #     if n not in ndict:
        #         ndict[n] = 0
        #     ndict[n] += 1
        # for key in ndict:
        #     if ndict[key] == 1:
        #         return key

        # O(n) time, O(1) space:
        single = 0
        for n in nums:
            single = single ^ n
        return single


sol = Solution()
n_arr = [4, 1, 2, 1, 2]
print(sol.singleNumber(n_arr))
