"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are
adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        pointer = 0
        for i in [0, 1, 2]:
            if i in counts:
                for _ in range(counts[i]):
                    nums[pointer] = i
                    pointer += 1
