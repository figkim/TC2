class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [('(', 1)]

        ans = []

        while len(stack) > 0:
            token, score = stack.pop()

            if score < 0:
                continue

            if len(token) == 2 * n:
                if score == 0:
                    ans.append(token)
                continue

            stack.append((token + '(', score + 1))
            stack.append((token + ')', score - 1))      
                
        return ans
