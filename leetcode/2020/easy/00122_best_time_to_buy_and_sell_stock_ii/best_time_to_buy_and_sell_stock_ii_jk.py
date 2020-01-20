class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        for i in range(len(prices)-1):
            max_profit += max(prices[i+1] - prices[i], 0)
            
        return max_profit
