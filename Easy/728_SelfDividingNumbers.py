"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        nums = range(left, right+1)
        results = []

        def _check_self_div(n):
            dividers = list(map(int, str(n)))
            for d in dividers:
                if d == 0 or n % d != 0:
                    return False
            return True

        for num in nums:
            if _check_self_div(num):
                results.append(num)

        return results


sol = Solution()
left = 1
right = 22
print(sol.selfDividingNumbers(left, right))

