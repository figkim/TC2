class Solution(object):
    def reverse(self, x):
        str_input = list(str(abs(x)))
        str_input.reverse()
        first_nonzero_checker = False
        temp = ''
        # reverse and iterate.
        # deal zero whether they met non-zero value or not until now.
        for n, i in enumerate(str_input):
            if i != '0':
                first_nonzero_checker = True
            elif i == '0' and not first_nonzero_checker:
                continue
            temp = temp + i
        
        # deal neg sign.
        if x < 0:
            temp = '-' + temp

        # deal problem condition
        if x == 0 or int(temp) < -2**31 or int(temp) > 2**31 - 1:
            return 0
            
        return int(temp)
