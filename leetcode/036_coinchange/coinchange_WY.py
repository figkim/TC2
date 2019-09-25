class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        nums = [0] * (amount + 1)
        nums[0] = 1
        for coin in coins:
            for val in range(1, amount + 1):
               if val >= coin:
                   nums[val] += nums[val - coin]
        return nums[-1]