class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        min_p = prices[0]
        
        for price in prices:
            min_p = min(min_p, price)
            profit = max(profit, price - min_p)
            
        return profit
