"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums, target: int) -> int:

        low = 0
        high = len(nums)-1

        #check borders
        if target < nums[low]:
            return -1
        if target > nums[high]:
            return -1

        middle = (high + low) // 2
        while target != nums[middle] and low <= high:

            if target < nums[middle]:
                high = middle - 1
            else:
                low = middle + 1
            middle = (high + low) // 2

        if target == nums[middle]:
            return middle
        else:
            return -1


sol = Solution()
arr = [-1, 0, 3, 5, 9, 12]
t = 9
print(sol.search(arr, t))

t = 2
print(sol.search(arr, t))

arr = [5]
t = 5
print(sol.search(arr, t))
