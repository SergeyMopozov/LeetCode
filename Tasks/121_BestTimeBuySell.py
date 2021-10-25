"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices) -> int:
        # 0(n^2)
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > profit:
        #             profit = prices[j] - prices[i]
        # return profit

        # O(n)
        profit = 0
        min_price = float('inf')

        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > profit:
                profit = p - min_price

        return profit



s = Solution()
p_arr = [7, 1, 7, 3, 6, 4]
print(s.maxProfit(p_arr))
