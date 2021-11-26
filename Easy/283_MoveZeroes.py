"""
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[j] != 0:
                j += 1
            elif nums[i] != 0 and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1



sol = Solution()
nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]
sol.moveZeroes(nums)
print(nums)

nums = [0]
#Output: [0]
sol.moveZeroes(nums)
print(nums)
