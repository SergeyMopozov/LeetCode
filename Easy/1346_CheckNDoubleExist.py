"""
Given an array arr of integers, check if there exists two integers N and M
such that N is the double of M ( i.e. N = 2 * M).
"""

class Solution:
    def checkIfExist(self, arr) -> bool:
        arr_dict = {}
        for idx, n in enumerate(arr):
            if n not in arr_dict:
                arr_dict[n] = idx

        for idx, n in enumerate(arr):
            if n * 2 in arr and arr_dict[n * 2] != idx:
                return True
        return False


sol = Solution()
arr = [10,2,5,3]
print(sol.checkIfExist(arr))

arr = [7,1,14,11]
print(sol.checkIfExist(arr))

arr = [-2,0,10,-19,4,6,-8]
print(sol.checkIfExist(arr))

arr = [0, 0]
print(sol.checkIfExist(arr))
