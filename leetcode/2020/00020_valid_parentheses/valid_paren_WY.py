class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        pars = {"(":")","[":"]","{":"}"}
        
        stack = list()
        
        for i,par in enumerate(s):
            if par in pars.keys():
                stack.append(par)
            elif (par in pars.values()) and (i > 0):
                if stack == []:
                    return False
                elif pars.get(stack[-1]) == par:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return stack == []