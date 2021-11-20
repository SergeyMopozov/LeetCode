"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums, target: int) -> int:

        low, high = 0, len(nums) - 1
        while low <= high:
            middle = (low + high) // 2

            if target == nums[middle]:
                return middle
            elif nums[middle] >= nums[low]:
                if nums[middle] > target >= nums[low]:
                    high = middle - 1
                else:
                    low = middle + 1
            else:
                if nums[middle] < target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1

        return -1


sol = Solution()
nums = [4, 5, 6, 7, 9, 0, 1, 2, 3]
target = 0

print(sol.search(nums, target))

#
# nums = [8, 0, 1, 2, 4, 5, 6, 7]
# target = 0
#
# print(sol.search(nums, target))
#
# nums = [8, 10, 0, 1, 2, 4, 5, 6, 7]
# target = 0
#
# print(sol.search(nums, target))
#
# nums = [0]
# target = 0
#
# print(sol.search(nums, target))
#
# nums = [1]
# target = 0
#
# print(sol.search(nums, target))

