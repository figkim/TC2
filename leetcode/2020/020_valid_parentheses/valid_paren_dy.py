class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = dict(zip("({[", "123"))
        closes = dict(zip(")}]", "123"))
        for i in s:
            if i in opens:
                stack.append(i)
            else:
                if stack and opens[stack[-1]] == closes[i]:
                    stack = stack[:-1]
                else:
                    return False
        if stack:
            return False
        return True
            
