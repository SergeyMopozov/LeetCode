"""
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence
(i.e. subarray).
The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r)
such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
"""

class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        long_s = 1
        curr_s = 1
        start = nums[0]
        for n in nums[1:]:
            if n > start:
                curr_s += 1
                start = n
            else:
                if curr_s > long_s:
                    long_s = curr_s
                curr_s = 1
                start = n
        if curr_s > long_s:
            long_s = curr_s
        return long_s


sol = Solution()
arr = [1, 2, 3, 5, 4, 7, 9, 10, 12, 13]
print(sol.findLengthOfLCIS(arr))
