class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        # buy not buy sell not sell
        reward = [-prices[0], 0, 0, -prices[0]]
        
        for price in prices[1:]:            
            reward = max(reward[1], reward[3]) - price, max(reward[1], reward[2]), max(reward[0], reward[3]) + price, max(reward[0], reward[3])
        
        return max(reward[1], reward[2])
