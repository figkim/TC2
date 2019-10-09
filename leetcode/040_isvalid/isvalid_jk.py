class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for c in s:
            if c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            else:
                stack.append(c)

        if len(stack):
            return False
        else:
            return True
