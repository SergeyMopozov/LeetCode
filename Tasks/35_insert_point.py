"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchInsert(self, nums, target):

        end = len(nums) - 1
        for i in range(len(nums)):

            if target == nums[i]:
                return i
            elif target == nums[end - i]:
                return end - i
            elif i+1 < len(nums) and nums[i] < target < nums[i+1]:
                return i+1
            elif end - i > 0 and nums[end - i - 1] < target < nums[end - i]:
                return end - i
            elif i == 0 and target < nums[i]:
                return i
            elif i == end and target > nums[end]:
                return end + 1
            elif i == len(nums) - 1 and target > nums[i]:
                return len(nums)
            elif i == 0 and target < nums[i]:
                return 0


s = Solution()

nums = [1, 3, 5, 6]
target = 5
print(s.searchInsert(nums, target))


nums = [1, 3, 5, 6]
target = 2
print(s.searchInsert(nums, target))

nums = [1, 3, 5, 6]
target = 7
print(s.searchInsert(nums, target))

nums = [1]
target = 0
print(s.searchInsert(nums, target))
