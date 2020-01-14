class Solution(object):
    memTable = {1:1, 2:2, 3:3}
    def climbStairs(self, n):
        """ consider and return whole possible ways to get the top of n-stairs.
        
            # arguments
                :type n: int, number of stairs
                
            # return
                :rtype: int, number of ways to make n with linear combination of 1 and 2.
        """
        if not self.memTable.get(n):
            self.memTable[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memTable[n]

