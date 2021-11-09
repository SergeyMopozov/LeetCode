"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # slow solution
        # for i in range(len(s)):
        #     if s[0:i] + s[i+1:] == (s[0:i] + s[i+1:])[::-1]:
        #         return True
        # return False

        # recursive solution
        def _isValid(st):
            if st == st[::-1]:
                return True

        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return _isValid(s[left:right]) or _isValid(s[left+1:right+1])

        return True
sol = Solution()
# string = 'abcca'
# print(sol.validPalindrome(string))
#
# string = 'abccdba'
# print(sol.validPalindrome(string))

string = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(sol.validPalindrome(string))

