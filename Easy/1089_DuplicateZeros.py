"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.
"""

class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        nums = arr.copy()
        insertion = 0
        for idx, n in enumerate(nums):
            if n == 0:

                arr.insert(idx+insertion+1, 0)
                arr.pop()
                insertion += 1



sol = Solution()
arr = [1,0,2,3,0,4,5,0]
#Output: [1,0,0,2,3,0,0,4]
sol.duplicateZeros(arr)
print(arr)

arr = [0,1,7,6,0,2,0,7]
# [0,0,1,7,6,0,0,2]
sol.duplicateZeros(arr)
print(arr)
