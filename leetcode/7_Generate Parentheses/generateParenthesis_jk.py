class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [('(', 1, 0)]

        ans = []

        while len(stack) > 0:
            token, left, right = stack.pop()

            if left + right == 2 * n:
                ans.append(token)
                continue

            if left < n:
                stack.append((token + '(', left + 1, right))

            if left > right:
                stack.append((token + ')', left, right + 1))     
                
        return ans
