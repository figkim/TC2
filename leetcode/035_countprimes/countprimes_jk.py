class Solution:
    def countPrimes(self, n: int) -> int:
        nums = set(range(2, n))
        
        for i in range(2, int(n**.5)+1):
            nums -= set(range(2*i, n, i))
            
        return len(nums)
