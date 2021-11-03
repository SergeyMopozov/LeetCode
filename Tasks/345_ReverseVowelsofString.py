"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.


"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        found = set()
        result = []
        for c in s:
            if c in vowels:
                if c in found:
                    pass




sol = Solution()
s = "hello" # "holle"
print(sol.reverseVowels(s))

s = 'leetcode' # "leotcede"
print(sol.reverseVowels(s))
