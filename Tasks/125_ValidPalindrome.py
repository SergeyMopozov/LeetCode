"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ignore spaces, punctuation and cases
        # compare string and its reverse

        chairs = []
        for c in s:
            if c.isalnum():
                chairs.append(c.lower())
        if ''.join(chairs) == ''.join(chairs[::-1]):
            return True
        else:
            return False


sol = Solution()
string = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(string))
