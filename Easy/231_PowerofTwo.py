"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        i = 0
        while i < 32:

            if n == 2 ** i:
                return True
            i += 1

        return False

    def isPowerOfTwoBit(self, n: int) -> bool:
        x = 1
        i = 0

        while i < 32:
            print(x)
            if n == x:
                return True
            x = 1 << i
            i += 1

        return False


sol = Solution()
num = 1
print(sol.isPowerOfTwo(num))
print(sol.isPowerOfTwoBit(num))

num = 2**4
print(sol.isPowerOfTwo(num))
print(sol.isPowerOfTwoBit(num))
