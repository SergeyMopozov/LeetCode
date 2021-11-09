"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = num
        while root**2 - num > 0.01:
            root = 1/2 * (root + num/root)

        if round(root)**2 - num == 0:
            return True
        return False


sol = Solution()
n = 14
print(sol.isPerfectSquare(n))

n = 16
print(sol.isPerfectSquare(n))
