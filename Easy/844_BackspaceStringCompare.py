"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        results = []
        for string in [s, t]:
            r = []
            for c in string:
                if c == '#':
                    if len(r) != 0:
                        r.pop()
                else:
                    r.append(c)
            results.append(''.join(r))

        if results[0] == results[1]:
            return True
        else:
            return False



sol = Solution()
s = "ab#c"
t = "ad#c"
print(sol.backspaceCompare(s, t))

s = "a#c"
t = "b"
print(sol.backspaceCompare(s, t))

s = "a##c"
t = "#a#c"
print(sol.backspaceCompare(s, t))
