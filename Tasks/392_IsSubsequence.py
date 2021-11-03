"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == '':
            return True

        second = 0
        for first in range(len(t)):
            if second < len(s):
                if t[first] == s[second]:
                    second += 1
        if second == len(s):
            return True
        return False

sol = Solution()
t = "aabcde"
s = "ace"
print(sol.isSubsequence(s, t))
s = "aec"
print(sol.isSubsequence(s, t))

s = "b"
t = "abc"
print(sol.isSubsequence(s, t))
