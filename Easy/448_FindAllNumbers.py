"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        # result = []
        # for n in range(1, len(nums)+1):
        #     if n not in nums:
        #         result.append(n)
        #
        # return result

        return list(set(range(1, len(nums)+1)).difference(set(nums)))


sol = Solution()
arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(sol.findDisappearedNumbers(arr))
