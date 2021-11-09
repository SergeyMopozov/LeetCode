"""
The Fibonacci numbers, commonly denoted F(n) form a sequence,
 the Fibonacci sequence, such that each number is the sum of the two preceding ones, s
 tarting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""

class Solution:
    def fib(self, n: int) -> int:
        # recursive solution
        # def _fib(n):
        #     if n == 0:
        #         return 0
        #     elif n == 1:
        #         return 1
        #     else:
        #         return _fib(n-1) + _fib(n-2)
        #
        # return _fib(n)

        # iterate solution
        if n == 0:
            return 0
        elif n == 1:
            return 1

        result = [0, 1]
        i = 2
        while i <= n:
            result.append(result[i-2] + result[i-1])
            i += 1

        return result[i-1]



sol = Solution()
n = 4
print(sol.fib(n))
