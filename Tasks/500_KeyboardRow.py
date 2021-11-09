"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
"""

class Solution:
    def findWords(self, words):
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')
        result = []
        for w in words:
            if set(w.lower()).issubset(first) or set(w.lower()).issubset(second) or set(w.lower()).issubset(third):
                result.append(w)

        return result


sol = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(sol.findWords(words))
