"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part.
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
[−2**31, 2**31 − 1]. For this problem, assume that your function returns 2**31 − 1 when the division result overflows.
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        sign = 1
        if (dividend < 0 < divisor) or (divisor < 0 < dividend):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            result = dividend * sign

            if result > 2**31 - 1 or result < -2**31:
                return 2**31 - 1
            else:
                return result

        while dividend - divisor >= 0:
            dividend = dividend - divisor
            result += 1

        result = result * sign

        if result > 2**31-1 or result < -2**31:
            return 2**31 - 1
        else:
            return result



s = Solution()

a, b = 10, 3
print(s.divide(a, b))

a, b = 7, -3
print(s.divide(a, b))

a, b = 0, 1
print(s.divide(a, b))

a, b = 1, 1
print(s.divide(a, b))

a = -2147483648
b = -1

print(s.divide(a, b))

# TODO too slow
a = 2147483647
b = 2

print(s.divide(a, b))