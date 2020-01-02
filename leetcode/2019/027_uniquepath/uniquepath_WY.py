class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        def factorial(k):
            if k == 0:
                return 1
            else:
                return k*factorial(k-1)
        
        def sub_factorial(k,l):
            if k == l:
                return 1
            else:
                return k*sub_factorial(k-1,l)
            
        min_val = min(m,n)
        
        return int(sub_factorial(m+n-2,m+n-2-min_val+1)/factorial(min_val-1))