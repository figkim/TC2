class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        else:
            if int(str(x)[-1::-1]) == x:
                return True
            else:
                False
