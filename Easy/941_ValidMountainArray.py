"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

class Solution:
    def validMountainArray(self, arr) -> bool:

        if len(arr) < 3:
            return False

        peak = False
        prev = arr[0]

        for idx, n in enumerate(arr[1:]):
            if idx != 0 and n < prev:
                peak = True
            if not peak:
                if n <= prev:
                    return False
            elif peak:
                if n >= prev:
                    return False

            if idx != 0 and n < prev:
                peak = True
            prev = n

        return peak and True



sol = Solution()
arr = [3,5,6,5,4,3]
print(sol.validMountainArray(arr))

arr = [1, 2]
print(sol.validMountainArray(arr))

arr = [9,8,7,6,5,4,3,2,1,0]
print(sol.validMountainArray(arr))

arr = [0,1,2,3,4,5,6]
print(sol.validMountainArray(arr))

arr = [4,4,3,2,1]
print(sol.validMountainArray(arr))
