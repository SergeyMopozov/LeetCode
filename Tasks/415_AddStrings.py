"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return int(num1) + int(num2)


sol = Solution()

num1 = "11"
num2 = "123"
print(sol.addStrings(num1, num2))
