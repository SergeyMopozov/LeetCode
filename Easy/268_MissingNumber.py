"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

"""


class Solution:
    def missingNumber(self, nums) -> int:
        n_dict = {}

        for n in nums:
            if n not in n_dict:
                n_dict[n] = 0
            n_dict[n] += 1

        for i in range(len(nums)+1):
            if i not in n_dict:
                return i

sol = Solution()
arr = [3, 0, 1, 4]
print(sol.missingNumber(arr))
