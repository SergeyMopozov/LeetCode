"""
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive)
of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.
"""

class Solution:
    def largeGroupPositions(self, s: str):
        # # 1. line search
        # start = 0
        # length = 1
        # start_c = s[0]
        # groups = []
        # for i in range(1, len(s)):
        #     if s[i] != start_c:
        #         if length >= 3:
        #             groups.append([start, start+length-1])
        #         start = i
        #         length = 1
        #         start_c = s[i]
        #     else:
        #         length += 1
        #
        # if length >= 3:
        #     groups.append([start, start + length - 1])
        #
        # return groups

        # 2. Two pointers

        groups = []
        start = 0
        for end in range(len(s)):
            if end == len(s) - 1 or s[end] != s[end+1]:
                if end - start + 1 >= 3:
                    groups.append([start, end])
                start = end + 1

        return groups



sol = Solution()
s = "abcdddeeeeaabbbcd"
print(sol.largeGroupPositions(s))

s = "aaa"
print(sol.largeGroupPositions(s))