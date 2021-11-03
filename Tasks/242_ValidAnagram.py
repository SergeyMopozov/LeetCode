"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}
        for c in s:
            if c not in s_chars:
                s_chars[c] = 0
            s_chars[c] += 1

        for c in t:
            if c not in t_chars:
                t_chars[c] = 0
            t_chars[c] += 1

        if s_chars == t_chars:
            return True
        else:
            return False


sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))

s = "rat"
t = "car"
print(sol.isAnagram(s, t))
