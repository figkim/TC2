class Solution(object):
   def evalRPN(self, tokens):
       """
       :type tokens: List[str]
       :rtype: int
       """
       i = 0
       symbols = ["+","-","*","/"]
       while i < len(tokens)-2:
           if tokens[i] not in symbols and tokens[i+1] not in symbols and tokens[i+2] not in symbols:
               i += 1
               continue
           else:
               if tokens[i+2] == "+":
                   num = int(tokens[i]) + int(tokens[i+1])
               elif tokens[i+2] == "-":
                   num = int(tokens[i]) - int(tokens[i+1])
               elif tokens[i+2] == "*":
                   num = int(tokens[i]) * int(tokens[i+1])
               elif tokens[i+2] == "/":
                   if int(tokens[i]) * int(tokens[i+1]) >= 0:
                       num = int(tokens[i]) // int(tokens[i+1])
                   else:
                       num = - (abs(int(tokens[i])) // abs(int(tokens[i+1])))
               tokens.pop(i+2)
               tokens.pop(i+1)
               tokens[i] = str(num)
               if i+1 < len(tokens) and tokens[i+1] in symbols:
                   i -= 1
       return int(tokens[0])