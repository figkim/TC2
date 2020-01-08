class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if (x < -2**31) or (x > 2**31 - 1):
            return 0
        else:
            rev_x = str(x)
            if rev_x[0] == "-":
                rev_x = int(rev_x[-1:0:-1])*(-1)
            else:
                rev_x = int(rev_x[-1::-1])
            if (rev_x < -2**31) or (rev_x > 2**31 - 1):
                return 0
            else:
                return rev_x