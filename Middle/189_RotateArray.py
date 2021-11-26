"""
Given an array, rotate the array to the right by k steps, where k is non-negative
"""

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # return nums[-k:] + nums[:-k]

        # k = k % len(nums)
        # for i in range(k):
        #     temp = nums[-1]
        #     for j in range(len(nums)-1, 0, -1):
        #         nums[j] = nums[j-1]
        #     nums[0] = temp

        def _reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        k = k % len(nums)
        _reverse(nums, 0, len(nums)-1)
        _reverse(nums, 0, k-1)
        _reverse(nums, k, len(nums)-1)





sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
#: [5,6,7,1,2,3,4]
sol.rotate(nums, k)
print(nums)
