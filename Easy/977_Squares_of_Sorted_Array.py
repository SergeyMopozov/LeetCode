"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares
of each number sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums):

        less_zero = []
        other = []
        result = []
        for n in nums:
            if n < 0:
                less_zero.append(n**2)
            else:
                other.append(n**2)

        less_zero = less_zero[::-1]
        p1 = p2 = 0
        for k in range(len(nums)):
            if p1 < len(less_zero) and (p2 == len(other) or less_zero[p1] < other[p2]):
                result.append(less_zero[p1])
                p1 += 1
            else:
                result.append(other[p2])
                p2 += 1

        return result



        # result = []
        # for n in nums:
        #     result.append(n * n)
        #
        # return sorted(result)


sol = Solution()
nums = [-4,-1,0,3,10]
print(sol.sortedSquares(nums))
