class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        prime_list = [False,False] + [True]*(n-1)
        
        for k in range(2,int(n**0.5) + 1):
            if prime_list[k]:
                for j in range(2,n/k + 1):
                    prime_list[j*k] = False
            
        return sum(prime_list[:-1])