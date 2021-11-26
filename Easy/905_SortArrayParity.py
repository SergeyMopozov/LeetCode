"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""


# def sortArrayByParity(self, A):
#        i, j = 0, len(A) - 1
#        while i < j:
#            if A[i] % 2 > A[j] % 2:
#                A[i], A[j] = A[j], A[i]
#
#            if A[i] % 2 == 0: i += 1
#            if A[j] % 2 == 1: j -= 1
#
#        return A


class Solution:
    def sortArrayByParity(self, nums):
        odd = []
        even = []

        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        return even + odd


sol = Solution()
nums = [3,1,2,4]
print(sol.sortArrayByParity(nums))