"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.


II Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

    def containsNearbyDuplicate(self, nums, k) -> bool:
        n_dict = {}
        for idx, n in enumerate(nums):
            if n not in n_dict:
                n_dict[n] = idx
            else:
                if abs(n_dict[n] - idx) <= k:
                    return True
                else:
                    n_dict[n] = idx
        return False




sol = Solution()
n = [1, 1, 2, 3]
print(sol.containsDuplicate(n))

nums = [1, 2, 3, 1]
k = 3
print(sol.containsNearbyDuplicate(nums, k))
