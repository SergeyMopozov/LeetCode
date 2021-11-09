"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max_con = 0
        curr_con = 0

        for n in nums:
            if n == 1:
                curr_con += 1
            elif n == 0:
                if curr_con > max_con:
                    max_con = curr_con
                curr_con = 0
        if curr_con > max_con:
            max_con = curr_con
        return max_con


sol = Solution()
n = [1,1,1,0,1,1,1,1,1,1,1,1,]
print(sol.findMaxConsecutiveOnes(n))
