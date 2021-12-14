"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get
a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

class Solution:
    def dailyTemperatures(self, temperatures):

        # O(n2) solution
        # result = []
        #
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] >temperatures[i]:
        #             result.append(j-i)
        #             break
        #
        #     if len(result) < len(temperatures[:i+1]):
        #         result.append(0)
        # return result

        n = len(temperatures)
        stack = []
        result = [0]*n

        for i in range(n-1, -1, -1):
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if len(stack) == 0:
                result[i] = 0
            else:
                result[i] = stack[-1] - i

            stack.append(i)

        return result






sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
# [1,1,4,2,1,1,0,0]
print(sol.dailyTemperatures(temperatures))
