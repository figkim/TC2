from math import gcd

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)

        def ugly_num_cnt(n, a, b, c):
            return n // a + n // b + n // c - n // lcm(a, b) - n // lcm(b, c) - n // lcm(a, c) + n // lcm(lcm(a, b), c)

        l = 1
        r = 2 * 10 ** 9

        while l < r:
            mid = l + (r - l) // 2
            if ugly_num_cnt(mid, a, b, c) < n:
                l = mid + 1
            else:
                r = mid
        return l
