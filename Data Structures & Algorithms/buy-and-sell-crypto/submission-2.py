class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0              # default: no profit
        min_price = float('inf')   # no price seen yet
        
        for price in prices:
            if price < min_price:          # new cheapest buy day?
                min_price = price          # update it
            
            profit = price - min_price     # profit if sell today
            max_profit = max(max_profit, profit)  # best profit so far
        
        return max_profit
        