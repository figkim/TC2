class Solution:
    def get_num(self, n: int) -> int:
        res = 0
        while n >= 10:
            n, r = divmod(n, 10)
            res += r**2

        res += n**2

        return res
    
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        hist = set([n])

        while True:    
            n = self.get_num(n)

            if n in hist:
                return False

            if n == 1:
                return True

            hist.add(n)
