"""
Given a characters array letters that is sorted in non-decreasing order and a character target,
return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
"""

class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:

        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        return letters[0]


sol = Solution()
letters = ["c","f","j"]
target = "a"
print(sol.nextGreatestLetter(letters, target))

letters = ["c","f","j"]
target = "c"
print(sol.nextGreatestLetter(letters, target))

letters = ["c","f","j"]
target = "d"
print(sol.nextGreatestLetter(letters, target))

letters = ["c","f","j"]
target = "g"
print(sol.nextGreatestLetter(letters, target))

letters = ["c","f","j"]
target = "j"
print(sol.nextGreatestLetter(letters, target))

