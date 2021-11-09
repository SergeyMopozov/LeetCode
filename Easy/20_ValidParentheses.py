"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s):
        pairs = {')': '(',
                 ']': '[',
                 '}': '{'}
        stack = []
        for ch in s:

            # check next character is closed breaks
            if len(stack) != 0 and ch in pairs:
                # if opened and closed breaks equal remove it
                if stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        if len(stack) == 0:
            return True
        else:
            return False




s1 = "()[]{}"
# Expected Output: True

s2 = "([)]"
# Expected Output: False

s3 = "({[)"
# Expected Output: False

solution = Solution()
print(solution.isValid(s1))
print(solution.isValid(s2))
print(solution.isValid(s3))
