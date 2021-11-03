"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        vocab = {}
        rev_vocab = {}
        if len(pattern) != len(words):
            return False

        for p, w in zip(pattern, words):
            if p not in vocab and w not in rev_vocab:
                vocab[p] = w
                rev_vocab[w] = p
            elif vocab.get(p) != w or rev_vocab.get(w) != p:
                return False
        return True


sol = Solution()
pat = "abba"
string = "dog cat cat dog"
print(sol.wordPattern(pat, string))

pat = "abba"
string = "dog dog dog dog"
print(sol.wordPattern(pat, string))
