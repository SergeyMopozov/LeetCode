"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters
onto the end of the merged string.

Return the merged string.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = []
        second = 0
        for first in word1:

            result.append(first)
            if second < len(word2):
                result.append(word2[second])
                second += 1

        if second < len(word2):
            result += list(word2[second:])

        return ''.join(result)


sol = Solution()
word1 = "abcdff"
word2 = "pqr"
#Output: "apbqcr"

print(sol.mergeAlternately(word1, word2))
