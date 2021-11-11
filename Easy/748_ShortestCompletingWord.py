"""
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate.
Ignore numbers and spaces in licensePlate, and treat letters as case insensitive.
If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice.
Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists.
If there are multiple shortest completing words, return the first one that occurs in words.
"""

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:

        def _is_completing(word, licence):
            word_c = {}
            for w in word.lower():
                if w not in word_c:
                    word_c[w] = 0
                word_c[w] += 1

            for k in licence:
                if k not in word_c or licence[k] > word_c[k]:
                    return False
            return True

        l_key = {}
        for c in licensePlate.lower():
            if c.isalpha():
                if c not in l_key:
                    l_key[c] = 0
                l_key[c] += 1

        min_len = float('inf')
        min_word = ''
        for w in words:
            if _is_completing(w, l_key):
                if len(w) < min_len:
                    min_len = len(w)
                    min_word = w

        return min_word


sol = Solution()
licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
print(sol.shortestCompletingWord(licensePlate, words))
