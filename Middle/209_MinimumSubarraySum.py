"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

class Solution:
    def minSubArrayLen(self, target, nums) -> int:

        # prefix = []
        # curr_sum = 0
        # for n in nums:
        #     curr_sum += n
        #     prefix.append(curr_sum)
        # answer = float('inf')
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         curr_sum = prefix[j] - prefix[i] + nums[i]
        #         if curr_sum >= target:
        #             answer = min(answer, j - i + 1)
        #
        # if answer != float('inf'):
        #     return answer
        # else:
        #     return 0

        curr_sum = 0
        left = 0
        answer = float('inf')

        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= target:
                answer = min(answer, i+1-left)
                curr_sum -= nums[left]
                left += 1

        if answer != float('inf'):
            return answer
        else:
            return 0


sol = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(sol.minSubArrayLen(target, nums))
