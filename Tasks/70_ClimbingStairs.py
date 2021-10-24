"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

class Solution:

    def climbStairs(self, n: int) -> int:

        # recursive solution
        # def _climbStairs(m):
        #     if m == 1:
        #         return 1
        #     elif m == 2:
        #         return 2
        #     else:
        #         return _climbStairs(m-1) + _climbStairs(m-2)
        #
        # return _climbStairs(n)

        count = [1, 2]

        for i in range(2, n):
            count.append(count[i-1] + count[i-2])

        return count[n-1]

s = Solution()
n = 38
print(s.climbStairs(n))
