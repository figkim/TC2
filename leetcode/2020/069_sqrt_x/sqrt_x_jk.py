class Solution:
    def mySqrt(self, x: int) -> int:        
        #return int(x**.5)
        
        if x == 0:
            return 0
        
        start = 1
        end = x
        
        while start < end - 1:
            mid = (start + end)//2
            
            if mid ** 2 <= x:
                start = mid
            else:
                end = mid
                
        return start
