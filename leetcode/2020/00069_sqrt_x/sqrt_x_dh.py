class Solution(object):
    def mySqrt(self, x):
        if not x:
            return 0
        num = 1
        while True:
            num += 1
            if x < num**2:
                return num - 1
