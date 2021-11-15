"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        s1_count = {}
        s2_count = {}

        for w in s1.split():
            # s1_count[w] = s1_count.get(w, 0) + 1
            if w not in s1_count:
                s1_count[w] = 0
            s1_count[w] += 1
        for w in s2.split():
            if w not in s2_count:
                s2_count[w] = 0
            s2_count[w] += 1

        result = []
        for w in s1_count:
            if s1_count[w] == 1 and w not in s2_count:
                result.append(w)
        for w in s2_count:
            if s2_count[w] == 1 and w not in s1_count:
                result.append(w)

        return result


sol = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(sol.uncommonFromSentences(s1, s2))
