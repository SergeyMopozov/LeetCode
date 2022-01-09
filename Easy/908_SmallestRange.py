"""
You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x
is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.
"""


class Solution:
    def smallestRangeI(self, nums, k: int) -> int:

        max_n = max(nums)
        min_n = min(nums)

        delta = max_n - min_n
        if delta - 2*k < 0:
            return 0
        else:
            return delta - 2 * k
        # for i in range(len(nums)):
        #     if abs(max_n - nums[i]) <= k:
        #         nums[i] = max_n
        #     else:
        #         nums[i] += k
        #
        # print(nums)
        # max_n = max(nums)
        # min_n = min(nums)

        # return max_n - min_n


sol = Solution()
nums = [1]
k = 0
print(sol.smallestRangeI(nums, k))

nums = [0,10]
k = 2
print(sol.smallestRangeI(nums, k))

nums = [1,3,6]
k = 3
print(sol.smallestRangeI(nums, k))
