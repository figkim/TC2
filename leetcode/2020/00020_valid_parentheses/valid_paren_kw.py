class Solution(object):
    def isValid(self, s):
        stack = ['#']
        mapping = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in mapping:
                cand_char = stack.pop()
                if cand_char == mapping[char]:
                    continue
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 1 else False