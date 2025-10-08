# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, holding):
            if i >= len(prices):
                return 0
            state = i,holding
            if state not in memo:
                if holding:
                    sell = dp(i + 2, False) + prices[i]
                    Hold = dp(i + 1, True)
                    memo[state] = max(sell, Hold)
                else:
                    buy = dp(i + 1, True) - prices[i]
                    skip = dp(i + 1, False) 
                    memo[state] = max(buy, skip)
                 
             
            return memo[state]
        return dp(0, False)

    