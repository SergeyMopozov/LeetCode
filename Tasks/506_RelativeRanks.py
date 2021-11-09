"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition.
All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score,
the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number
(i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.
"""

class Solution:
    def findRelativeRanks(self, score):
        result = []
        sorted_score = sorted(score, reverse=True)
        for s in score:
            idx = sorted_score.index(s) + 1
            if  idx == 1:
                result.append('Gold Medal')
            elif idx == 2:
                result.append('Silver Medal')
            elif idx == 3:
                result.append('Bronze Medal')
            else:
                result.append(str(idx))
        return result


sol = Solution()
score = [5,4,3,2,1]
print(sol.findRelativeRanks(score))
