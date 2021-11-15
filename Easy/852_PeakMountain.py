"""
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain,
return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
"""

class Solution:
    def peakIndexInMountainArray(self, arr):

        prev = arr[0]
        p_idx = 0
        for idx, h in enumerate(arr[1:], 1):
            if h < prev:
                return p_idx

            else:
                prev = h
                p_idx = idx


sol = Solution()
arr = [3,4,5,1]
print(sol.peakIndexInMountainArray(arr))
