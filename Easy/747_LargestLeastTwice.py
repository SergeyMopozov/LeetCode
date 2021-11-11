"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, or return -1 otherwise.
"""


class Solution:
    def dominantIndex(self, nums) -> int:

        largest = 0

        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]

        for i in range(len(nums)):
            if nums[i] != largest:
                if largest < nums[i] * 2:
                    return -1
        return nums.index(largest)


sol = Solution()
arr = [3,6,1,0]
print(sol.dominantIndex(arr))

arr = [1]
print(sol.dominantIndex(arr))
