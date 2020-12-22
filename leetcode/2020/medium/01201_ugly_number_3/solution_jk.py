import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        lcm = lambda x, y : x * y // math.gcd(x, y)
        cnt = lambda num : num//a + num//b + num//c - num//lcm(a, b) - num//lcm(b, c) - num//lcm(c, a) + num//lcm(lcm(a, b), c)

        l = min(a, b, c)
        r = n*a + 1

        while l < r:
            mid = (l+r)//2
            u_mid = cnt(mid)

            if u_mid == n:
                break

            if u_mid > n:
                r = mid
            else:
                l = mid 
                
        while cnt(mid) == n and all([mid%a, mid%b, mid%c]):
            mid -= 1
            
        return mid
