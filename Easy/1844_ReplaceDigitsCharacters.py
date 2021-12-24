"""
You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = []

        for i in range(len(s)):
            if i % 2 == 1:
                result.append(alphabet[int(s[i]) + alphabet.index(s[i-1])])
            else:
                result.append(s[i])

        return ''.join(result)


sol = Solution()
s = "a1c1e1"
#Output: "abcdef"
print(sol.replaceDigits(s))

s = "a1b2c3d4e"
# "abbdcfdhe"
print(sol.replaceDigits(s))