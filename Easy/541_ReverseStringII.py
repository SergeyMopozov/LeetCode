"""
Given a string s and an integer k, reverse the first k characters for every 2k
characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        for i in range(0, len(s), 2*k):
            result.append(s[i:i+k][::-1])
            result.append(s[i+k:i + 2*k])

        return ''.join(result)



sol = Solution()
s = "abcdefg"
k = 2   #Output: "bacdfeg"
print(sol.reverseStr(s, k))
