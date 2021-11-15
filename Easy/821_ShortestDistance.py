"""
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length
and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
"""

class Solution:
    def shortestToChar(self, s: str, c: str):

        result = []
        c_inc = []
        for idx, letter in enumerate(s):
            if letter == c:
                c_inc.append(idx)

        curr = 0
        curr_c = c_inc[curr]
        for idx, letter in enumerate(s):
            if curr < len(c_inc)-1:
                if abs(idx - c_inc[curr]) > abs(idx - c_inc[curr+1]):
                    curr += 1
                    curr_c = c_inc[curr]
                else:
                    curr_c = c_inc[curr]

            result.append(abs(idx-curr_c))

        return result


sol = Solution()
s = "loveleetcode"
c = "e"
print(sol.shortestToChar(s, c))

