"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        for i in range(len(s)):
            if s[-1-i:] + s[:-1-i] == goal:
                return True
        return False



sol = Solution()
s = "abcde"
goal = "cdeab"
print(sol.rotateString(s, goal))
