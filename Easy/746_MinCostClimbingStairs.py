"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.

Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""


class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        final = [0]*(len(cost))
        final[-1] = cost[-1]
        final[-2] = cost[-2]
        for i in range(len(cost)-3, -1, -1):
            final[i] = cost[i] + min(final[i+1], final[i+2])

        return min(final[0], final[1])


sol = Solution()
cost = [10,15,20]
print(sol.minCostClimbingStairs(cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print(sol.minCostClimbingStairs(cost))
