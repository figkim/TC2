class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        queue = []
        op = ['+', '-', '*', '/']
        
        for sym in tokens:
            if sym not in op:
                queue.append(int(sym))
            else:
                num2 = queue.pop()
                num1 = queue.pop()

                if sym == '+':
                    res = num1 + num2
                elif sym == '-':
                    res = num1 - num2
                elif sym == '*':
                    res = num1 * num2
                elif sym == '/':
                    res = int(num1 / num2)

                queue.append(res)
                    
        return queue[-1]
