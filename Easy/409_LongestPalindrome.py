"""
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_count = {}

        for c in s:
            if c not in s_count:
                s_count[c] = 0
            s_count[c] += 1

        max_odd = 0
        palindrome_len = 0
        for c in s_count:
            if s_count[c] % 2 == 0:
                palindrome_len += s_count[c]
            elif s_count[c] % 2 == 1:
                if max_odd < s_count[c]:
                    max_odd = s_count[c]
                palindrome_len += s_count[c] - 1

        if max_odd != 0:
            palindrome_len += 1

        return palindrome_len


sol = Solution()
string = "abccccdd"
print(sol.longestPalindrome(string))
