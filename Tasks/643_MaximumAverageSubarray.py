"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
"""

class Solution:
    def findMaxAverage(self, nums, k: int) -> float:

        # #sliding window
        # max_avg = float('-inf')
        # for i in range(0, len(nums)):
        #     if len(nums[i:i+k]) == k:
        #
        #         avg = sum(nums[i:i+k]) / k
        #         if avg > max_avg:
        #             max_avg = avg
        #
        # return max_avg

        curr_sum = 0
        max_avg = float('-inf')
        start = 0

        for end in range(len(nums)):
            curr_sum += nums[end]
            if end >= k-1:
                max_avg = max(curr_sum/k, max_avg)
                curr_sum -= nums[start]
                start += 1
        return max_avg


sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(sol.findMaxAverage(nums, k))

nums = [4,0,4,3,3]
k = 5
print(sol.findMaxAverage(nums, k))
