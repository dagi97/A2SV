# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        hold = -prices[0]
        cash = 0

        for i in range(1, len(prices)):

            hold = max(hold, cash - prices[i])
            cash = max(cash,  prices[i] +  hold - fee )

        return cash 

         
        