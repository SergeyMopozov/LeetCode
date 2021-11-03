"""
Given two stings ransomNote and magazine,
return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = {}
        mag = {}

        for word in magazine:
            if word not in mag:
                mag[word] = 0
            mag[word] += 1

        for word in ransomNote:
            if word not in r:
                r[word] = 0
            r[word] += 1

        for word in r:
            if word not in mag or mag[word] < r[word]:
                return False

        return True

sol = Solution()

ran = 'aa'
m = 'aab'
print(sol.canConstruct(ran, m))

ran = 'ab'
m = 'aac'
print(sol.canConstruct(ran, m))