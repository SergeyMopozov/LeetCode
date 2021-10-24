"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        root = x
        while root * root - x > 0.5:
            root = 1 / 2 * (root + x/root)

        return round(root//1)



s = Solution()

d = 3

print(s.mySqrt(d))


