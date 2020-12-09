import operator
OPS = {"+": operator.add, "-": operator.sub,
       "*": operator.mul, "/": operator.truediv}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        
        for elem in tokens:
            if elem not in list(OPS.keys()):
                num_stack.append(int(elem))
            else:
                b, a = num_stack.pop(), num_stack.pop()
                num_stack.append(int(OPS[elem](a, b)))
        
        return num_stack.pop() 
