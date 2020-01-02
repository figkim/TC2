class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [0] + [amount + 1] * amount

        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        if dp[-1] == amount + 1:
            return -1
        
        else:
            return dp[-1]