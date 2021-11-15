"""
iven a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if not s[l].isalpha():
                l += 1
            if not s[r].isalpha():
                r -= 1
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return ''.join(s)


sol = Solution()
s = "Test1ng-Leet=code-Q!"  # Output: "Qedo1ct-eeLg=ntse-T!"
print(sol.reverseOnlyLetters(s))
