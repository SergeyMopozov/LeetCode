"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""


class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]

        curr_sum = 0
        for n in nums:
            curr_sum += n
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0: # start sum from new position of n
                curr_sum = 0

        return max_sum

s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums))

nums = [1]
print(s.maxSubArray(nums))

nums = [5, 4, -1, 7, 8]
print(s.maxSubArray(nums))

