"""
Given a non-empty array of non-negative integers nums, the degree of
this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
"""

class Solution:
    def findShortestSubArray(self, nums) -> int:
        degree = 0
        left_n = {}
        right_n = {}
        count_n = {}
        for i, n in enumerate(nums):
            if n not in left_n:
                left_n[n] = i
            right_n[n] = i
            if n not in count_n:
                count_n[n] = 0
            count_n[n] += 1
            if count_n[n] >= degree:
                degree = count_n[n]

        result = len(nums)
        for k in count_n.keys():
            if count_n[k] == degree:
                result = min(result, right_n[k]-left_n[k]+1)

        return result


sol = Solution()
arr = [1, 2, 2, 3, 1]
print(sol.findShortestSubArray(arr))
