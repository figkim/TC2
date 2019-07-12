class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        # use x-ary allowing each digit can be negative value
        # target = a_d * x**d + a_{d-1} * x**(d-1) + ... + a_0
        # n, k_i are integers in (-x,x)
        # divide into two cases
        # (case 1) a_i >= 0
        # (case 2) a_i < 0 by use the form x**(i+1) - b_i * x**i so that a_i = - b_i
        
        digit = 0
        while True:
            if x**digit <= target < x**(digit+1):
                break
            else:
                digit += 1
        
        case1 = -1
        case2 = digit
        
        while digit > 0:
            quotient = target/(x**digit)
            if target%(x**digit) == 0:
                return min(case1 + quotient*digit, case2 + (x-quotient)*digit, case1 + (quotient+1)*digit)
            case1, case2 = min(case1 + quotient*digit, case2 + (x-quotient)*digit), min(case1 + (quotient+1)*digit, case2 + (x-quotient-1)*digit)
            target %= x**digit
            digit -= 1
        
        quotient = target/(x**digit)
        
        return min(case1 + quotient*2, case2 + (x-quotient)*2, case1 + (quotient+1)*2, case2 + (x-quotient)*2)
        
        