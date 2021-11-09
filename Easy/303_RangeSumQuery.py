"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left
and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""


class NumArray:

    def __init__(self, nums):
        self.prefix = [0]
        for i in range(1, len(nums)+1):
            self.prefix.append(self.prefix[i-1]+nums[i-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
#   [0, -2, -2,
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
for left, right in [[0, 2], [2, 5], [0, 5]]:
    print(obj.sumRange(left, right))
