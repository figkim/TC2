class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        for i in range(len(y)//2+1):
            if y[i] == y[-(i+1)]:
                pass
            else:
                return False
        return True
