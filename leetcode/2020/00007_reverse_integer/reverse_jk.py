class Solution:
    def reverse(self, x: int) -> int:        
        ans = int(str(x)[::-1]) if x > 0 else -int(str(abs(x))[::-1])
        
        if x > 2**31-1 or x < -2**31 or ans > 2**31-1 or ans < -2**31:
            return 0
    
        return ans
