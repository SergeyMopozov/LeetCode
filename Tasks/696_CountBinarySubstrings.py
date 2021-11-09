"""
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        result = 0
        prev = 0
        curr = 1

        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                result += min(prev, curr)
                prev = curr
                curr = 1

            else:
                curr += 1
        return result + min(prev, curr)




sol = Solution()
string = "00110011"
print(sol.countBinarySubstrings(string))