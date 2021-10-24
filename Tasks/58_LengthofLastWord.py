"""
Given a string s consisting of some words separated by some number of spaces,
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()

        return len(s[-1])




solution = Solution()
string = "   fly me   to   the moon  "
print(solution.lengthOfLastWord(string))


