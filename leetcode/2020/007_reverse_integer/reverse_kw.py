class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x>=0 else -1
        rev_x = sign*int(str(sign*x)[::-1])
        return rev_x if -1*(2**31)-1<rev_x <2**31 else 0
