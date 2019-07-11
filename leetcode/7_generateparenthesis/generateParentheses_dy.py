class Solution:
    def insertParen(self, paren, cursor):
        if len(paren) == cursor:
            return paren + "()"
        return paren[:cursor] + "()" + paren[cursor:]
    
    def travel(self, paren, cursor, n, k):
        if n==k:
            return [paren]
        ans = []
        for i in range(cursor, len(paren)+1):
            if i == len(paren) or paren[i] == ")":
                new_paren = self.insertParen(paren, i)
                ans.extend(self.travel(new_paren, i+1, n, k+1))
        return ans
            
    def generateParenthesis(self, n: int) -> List[str]:
        ans = self.travel("", 0, n, 0)
        return ans
