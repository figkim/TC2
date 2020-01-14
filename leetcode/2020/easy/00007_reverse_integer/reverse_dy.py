class Solution:
    def reverse(self, x: int) -> int:
        y = str(abs(x))
        y = y[::-1]
        z = 1 * int(y) if x > 0 else -1 * int(y)
        if -2**31 <= z < 2**31:
            return z
        else:
            return 0
        
