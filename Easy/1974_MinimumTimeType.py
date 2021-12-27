"""
There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer.
A character can only be typed if the pointer is pointing to that character.
The pointer is initially pointing to the character 'a'.
"""


class Solution:
    def minTimeToType(self, word: str) -> int:

        alph = 'abcdefghijklmnopqrstuvwxyz'
        seconds = 0
        pointer = 0

        for ch in word:
            if ch != alph[pointer]:
                idx = alph.index(ch)
                if idx > pointer:
                    step = min(abs(idx - pointer), len(alph) - idx + pointer)
                else:
                    step = min(abs(idx - pointer), len(alph) - pointer + idx)
                seconds += step
                pointer = idx
            seconds += 1

        return seconds


sol = Solution()
word = "bza"
print(sol.minTimeToType(word))
word = "zjpc"
print(sol.minTimeToType(word))