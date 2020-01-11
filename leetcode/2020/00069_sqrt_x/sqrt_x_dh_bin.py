class Solution(object):
    def mySqrt(self, x):
        """ find and return sqrt(x).
        
            # arguments:
                x: integer, input.
                
            # return:
                num: integer, truncated value of sqrt(x) b/c return type is `int`.
        
        """
        if x == 1:
            return 1
        l = 0
        r = x
        while True:
            mid = (l + r) // 2
            
            if r-l == 1:
                return l
            elif mid **2 == x:
                return mid
            elif mid**2 >= x:
                r = mid
            else:
                l = mid
