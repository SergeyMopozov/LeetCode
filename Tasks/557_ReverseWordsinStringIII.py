"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
and initial word order.
"""

class Solution:
    def reverseWords(self, s: str) -> str:

        result = []
        for w in s.split():
            result.append(w[::-1])
        return ' '.join(result)


sol = Solution()
string = "Let's take LeetCode_Easy contest"
print(sol.reverseWords(string))
