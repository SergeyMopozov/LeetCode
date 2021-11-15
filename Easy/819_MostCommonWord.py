"""
Given a string paragraph and a string array of the banned words banned,
return the most frequent word that is not banned.
It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        # prepare string
        for i in "!?',;.":
            paragraph = paragraph.replace(i, '')
        paragraph = paragraph.lower().split()

        # count words
        word_count = {}
        for w in paragraph:
            if w not in word_count:
                word_count[w] = 0
            word_count[w] += 1

        for b in banned:
            if b in word_count:
                del word_count[b]

        max_freq = max(word_count.values())
        for k in word_count:
            if word_count[k] == max_freq:
                return k

sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sol.mostCommonWord(paragraph, banned))
