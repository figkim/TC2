class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        # naive and slow solution
        # try all possible cases by adding "(" and ")", repectively using set()
        
        if n == 1:
            return ["()"]
        else:
            temp1 = set()
            for possible in self.generateParenthesis(n-1):
                temp2 = set()
                for i in range(len(possible)+1):
                    fake = list(possible)
                    fake.insert(i,"(")
                    if "".join(fake) not in temp2:
                        temp2.add(("".join(fake),i))
                for string,value in temp2:
                    for j in range(value+1,len(possible)+2):
                        fake = list(string)
                        fake.insert(j,")")
                        temp1.add("".join(fake))
            return list(temp1)
        
        """
        # use recurrence relation
        # choose the first "(" and the k-th ")" 
        # then, in the middle of the two "(" and ")", there are exactly (k-1) well-performed parentheses
        # for the rest (n-k) well-performed parentheses, the lie on the right side of the k-th ")"
        
        if n == 0:
            return [""]
        elif n == 1:
            return ["()"]
        else:
            parenthses_list = list()
            for i in range(n):
                for str1 in self.generateParenthesis(i):
                    for str2 in self.generateParenthesis(n-1-i):
                        parenthses_list.append("("+str1+")"+str2)
            return parenthses_list

        """
        # JK's solution

        def generateParenthesis(self, n: int) -> List[str]:
            stack = [('(', 1, 0)]

            ans = []

            while len(stack) > 0: # cumulatively add possible puzzles #keyworkds: stack, DFS
                token, left, right = stack.pop()

                if left + right == 2 * n:
                    ans.append(token)
                    continue

                if left < n:
                    stack.append((token + '(', left + 1, right))

                if left > right:
                    stack.append((token + ')', left, right + 1))     
                    
            return ans
        """