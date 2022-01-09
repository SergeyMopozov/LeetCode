"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
"""


class Solution:
    def frequencySort(self, nums):
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1

        nums = sorted(nums, key=lambda n: (counter[n], -n), reverse=False)
        return nums


sol = Solution()
nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
print(sol.frequencySort(nums))

nums = [2,3,1,3,2]
#Output: [1,3,3,2,2]
print(sol.frequencySort(nums))

nums = [-1,1,-6,4,5,-6,1,4,1]
#Output: [5,-1,4,4,-6,-6,1,1,1]
print(sol.frequencySort(nums))
