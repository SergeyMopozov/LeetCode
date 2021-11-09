"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() a
nd Java's indexOf().
"""


class Solution:
    def strStr(self, haystack: str, needle: str):

        if needle == '' and haystack == '':
            return 0

        n_len = len(needle)
        for i in range(len(haystack) - n_len + 1):
            if haystack[i:i+n_len] == needle:
                return i
        return -1


s = Solution()

h = "hello"
n = "ll"
print(s.strStr(h, n))

h = "a"
n = "a"
print(s.strStr(h, n))
