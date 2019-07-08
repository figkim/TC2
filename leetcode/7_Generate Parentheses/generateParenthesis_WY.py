class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # naive and slow solution
        # try all possible cases by adding "(" and ")", repectively using set()
        
        if n == 1:
            return ["()"]
        else:
            temp1 = set()
            for possible in self.generateParenthesis(n-1):
                temp2 = set()
                for i in range(len(possible)+1):
                    fake = list(possible)
                    fake.insert(i,"(")
                    if "".join(fake) not in temp2:
                        temp2.add(("".join(fake),i))
                for string,value in temp2:
                    for j in range(value+1,len(possible)+2):
                        fake = list(string)
                        fake.insert(j,")")
                        temp1.add("".join(fake))
            return list(temp1)
        
        
        