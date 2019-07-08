class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(token):
            cnt = 0

            for sym in token:
                if sym == '(':
                    cnt += 1
                else:
                    cnt -= 1

                if cnt < 0:
                    return False

            return cnt == 0

        stack = ['(']
        ans = []

        while len(stack) > 0:
            token = stack.pop()
            
            if len(token) == 2 * n:
                if valid(token):
                    ans.append(token)
                    
                continue

            stack.append(token + '(')
            stack.append(token + ')')        
                
        return ans
