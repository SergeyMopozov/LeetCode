"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = {}
        for c in s:
            if c not in char:
                char[c] = 0
            char[c] += 1

        for idx, c in enumerate(s):
            if char[c] == 1:
                return idx
        return -1

sol = Solution()

string = 'aasdmwexee'
print(sol.firstUniqChar(string))
