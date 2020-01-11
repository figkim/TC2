class Solution(object):
    def bintotenary(self, a):
        """ convert string binary expression into integer 10-ary number.
        
            # arguments
                a: String, an binary number expression
            
            # return
                num: Int, 10-ary conversion of a.
        """
        return sum([int(j) * 2**i for i, j in enumerate(a[::-1])])
    
    
    def tenarytobin(self, a):
        """ convert 10-ary number to string binary expression 
        
            # arguments
                a: int, input 10-ary number to convert
                
            # return
                num: String, binary conversion of a.
        """
        if a == 1:
            return '1'
        
        num = ''
        quo, remains = a // 2, a % 2
        
        while True:
            num += str(remains)
            if quo == 0:
                break
            else:
                remains = quo % 2
                quo = quo // 2
        return num[::-1]
            
    
    def addBinary(self, a, b):
        return self.tenarytobin(self.bintotenary(a) + self.bintotenary(b))
