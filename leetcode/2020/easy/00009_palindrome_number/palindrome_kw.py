class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x%10 == 0 and x!=0):
            return False
        rev_x = 0
        while x > rev_x:
            rev_x = rev_x*10 + x%10
            x //= 10
        return rev_x == x or rev_x//10 == x