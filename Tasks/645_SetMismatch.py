"""
You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""


class Solution:
    def findErrorNums(self, nums):
        n_count = {}
        double = None
        for n in nums:
            if n not in n_count:
                n_count[n] = 0
            n_count[n] += 1
            if n_count[n] == 2:
                double = [n]

        miss = list(set(range(1, len(nums)+1)).difference(set(nums)))

        return double + miss


sol = Solution()
n_arr = [1, 2, 2, 4]
print(sol.findErrorNums(n_arr))

n_arr = [1,1]
print(sol.findErrorNums(n_arr))
