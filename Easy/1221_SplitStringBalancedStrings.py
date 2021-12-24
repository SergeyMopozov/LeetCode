"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_count = 0
        r_count = 0
        sub_count = 0

        for char in s:
            if char == 'R':
                r_count += 1
            elif char == 'L':
                l_count += 1

            if r_count - l_count == 0:
                sub_count += 1

        return sub_count



sol = Solution()
s = "RLRRLLRLRL"
#Output: 4
print(sol.balancedStringSplit(s))
