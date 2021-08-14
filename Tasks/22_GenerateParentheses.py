"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

1 <= n <= 8
"""


class Solution:

    def generateParantheses(self, n):
        # #1 Brute force
        # 1. Generate all possible combination
        # 2. chek it on valid and return only valid combinations

        def _genPar(s, pos, opened, closed, n, res):
            if closed == n:
                res.append(''.join(s))
                return
            else:
                if opened < n:
                    s[pos] = '('
                    _genPar(s, pos+1, opened+1, closed, n, res)
                if opened > closed:
                    s[pos] = ')'
                    _genPar(s, pos+1, opened, closed+1, n, res)

        result = []
        _genPar([''] * 2 * n, 0, 0, 0, n, result)
        return result


# test cases
# Input: n=1
# Output: ['()']
# Input: n=2
# Output: ['()()', '(())']
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

s = Solution()
for i in range(1, 5):
    print(s.generateParantheses(i))

