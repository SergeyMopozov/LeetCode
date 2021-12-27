"""
A permutation perm of n + 1 integers of all the integers in the range [0, n]
can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm,
return any of them.
"""

class Solution:
    def diStringMatch(self, s: str):

        pool = list(range(len(s)+1))
        low = 0
        big = len(s)
        perm = []
        for ch in s:
            if ch == 'I':
                perm.append(pool[low])
                low += 1
            elif ch == 'D':
                perm.append(pool[big])
                big -= 1

        perm.append(low)

        return perm




sol = Solution()
s = "IDID"
#Output: [0,4,1,3,2]
print(sol.diStringMatch(s))

s = "III"
#Output: [0,1,2,3]
print(sol.diStringMatch(s))

s = "DDI"
#Output: [3,2,0,1]
print(sol.diStringMatch(s))
