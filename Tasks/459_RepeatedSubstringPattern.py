"""
Given a string s, check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together.
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        start = 0
        for end in range(1, len(s)//2 + 1):
            pattern = s[start:end]

            if pattern * (len(s) // len(pattern)) == s:
                return True
        return False



sol = Solution()
string = 'ababac'
print(sol.repeatedSubstringPattern(string))

string = 'abcab'
print(sol.repeatedSubstringPattern(string))

string = "abcabcabcabc"
print(sol.repeatedSubstringPattern(string))
