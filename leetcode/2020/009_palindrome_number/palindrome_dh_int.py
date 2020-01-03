class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        tester = 1
        while True:
            if x / (tester * 10) < 1:
                break
            else:
                tester *= 10
                
        numlist = []
        xc = x
        while tester >= 1:
            tnum = xc // tester
            numlist.append(tnum)
            xc = xc - tnum * tester
            tester //= 10
            
        for nor, rev in zip(numlist, numlist[::-1]):
            if nor != rev:
                return False
        return True
