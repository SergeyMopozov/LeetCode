"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchRange(self, nums, target):

        # # O(n) approach
        # start = -1
        # end = -1
        #
        # if len(nums) == 0:
        #     return [start, end]
        #
        # for idx, n in enumerate(nums):
        #     if n == target and start == -1:
        #         start = idx
        #     if n != target and start != -1 and end == -1:
        #         end = idx - 1
        #
        # if n == target:
        #     end = idx
        #
        # return [start, end]

        # O(logn) aproach

        start, end = -1, -1
        # find start
        low, high = 0, len(nums) - 1
        while low <= high:

            middle = (low + high) // 2
            if target == nums[middle]:
                if middle > low and nums[middle - 1] == target:
                    high = middle - 1
                else:
                    start = middle
                    break
            elif target < nums[middle]:
                high = middle - 1
            else:
                low = middle + 1

        # find end
        low, high = 0, len(nums) - 1
        while low <= high:

            middle = (low + high) // 2
            if target == nums[middle]:
                if middle < high and nums[middle + 1] == target:
                    low = middle + 1
                else:
                    end = middle
                    break
            elif target < nums[middle]:
                high = middle - 1
            else:
                low = middle + 1

        return [start, end]


sol = Solution()
nums = [5,7,7,8,8,10]
target = 8
#Output: [3,4]
print(sol.searchRange(nums, target))

sol = Solution()
nums = [5,7,7,8,8,8]
target = 8
#Output: [3,5]
print(sol.searchRange(nums, target))


nums = [5,7,7,8,8,10]
target = 6
#Output: [-1,-1]
print(sol.searchRange(nums, target))

nums = []
target = 0
#Output: [-1,-1]
print(sol.searchRange(nums, target))

nums = [1]
target = 1
#Output: [0, 0]
print(sol.searchRange(nums, target))
