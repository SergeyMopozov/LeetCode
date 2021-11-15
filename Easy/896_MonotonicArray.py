"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""

class Solution:
    def isMonotonic(self, nums) -> bool:

        def _increase(nums):
            prev = nums[0]
            for n in nums[1:]:
                if n >= prev:
                    prev = n
                else:
                    return False
            return True

        def _decrease(nums):
            prev = nums[0]
            for n in nums[1:]:
                if n <= prev:
                    prev = n
                else:
                    return False
            return True

        if _decrease(nums) or _increase(nums):
            return True
        else:
            return False


sol = Solution()
nums = [1,2,2,3]
print(sol.isMonotonic(nums))

nums = [6, 5, 4, 4]
print(sol.isMonotonic(nums))


nums = [1,3,2]
print(sol.isMonotonic(nums))