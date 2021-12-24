"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        is_inter = True
        p1 = 0
        p2 = 0

        for c in s3:
            if p1 < len(s1) and c == s1[p1]:
                p1 += 1
            elif p2 < len(s2) and c == s2[p2]:
                p2 += 1
            else:
                print(p1, p2, c)
                is_inter = False
        if p1 != len(s1) or p2 != len(s2):
            print('last chance')
            is_inter = False

        return is_inter


sol = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(sol.isInterleave(s1, s2, s3))
