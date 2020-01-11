class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0, 1]
        
        for i in range(n):
            steps[0], steps[1] = steps[1], steps[0] + steps[1]
            
        return steps[-1]
