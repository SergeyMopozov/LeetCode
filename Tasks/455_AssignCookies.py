"""
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.

Each child i has a greed factor g[i],
which is the minimum size of a cookie that the child will be content with;
and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i,
and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number.
"""

class Solution:
    def findContentChildren(self, g, s) -> int:

        g = sorted(g)
        s = sorted(s)

        count = 0
        i = 0
        j = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
        return count



sol = Solution()
g = [1, 2, 3]
s = [1, 1]
print(sol.findContentChildren(g, s))
