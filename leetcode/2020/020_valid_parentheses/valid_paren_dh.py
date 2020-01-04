class Solution(object):
    close_paren_pair = {
                    ')': '(',
                    '}': '{',
                    ']': '[',
                 }

    def isValid(self, s):
        stack = []
        for p in s:
            if (len(stack) != 0) and (p in self.close_paren_pair) and (stack[-1] == self.close_paren_pair[p]):
                stack.pop()
            else:
                stack.append(p)
        if len(stack) == 0:
            return True
        else:
            return False
