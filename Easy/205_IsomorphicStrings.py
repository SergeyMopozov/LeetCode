"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        t_dict = {}
        s_dict = {}
        for s_c, t_c in zip(s, t):
            if t_c not in t_dict:
                t_dict[t_c] = s_c

            if s_c not in s_dict:
                s_dict[s_c] = t_c

        convert_t = []
        for c in t:
            convert_t.append(t_dict[c])

        convert_s = []
        for c in s:
            convert_s.append(s_dict[c])

        if ''.join(convert_t) == s and ''.join(convert_s) == t:
            return True
        else:
            return False


sol = Solution()
s = "egg"
t = "add"
print(sol.isIsomorphic(s, t))

s = "foo"
t = "bar"
print(sol.isIsomorphic(s, t))
