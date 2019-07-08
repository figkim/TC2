import re

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        cand = '('
        sol_list = []
        sol_list = self.make_sol(cand, n, sol_list)

        return sol_list

    def is_safe(self, cand, n):
        # check wheter given candidate is well defined or not
        left_idx = [m.start() for m in re.finditer('\(', cand)]
        right_idx = [m.start() for m in re.finditer('\)', cand)]
        if len(left_idx) <= n:
            if len(left_idx) >= len(right_idx):
                diff = [m2 - m1 for m1, m2 in zip(left_idx, right_idx)]
                return all(i >= 0 for i in diff)
            else:
                return False
        else:
            return False

    def make_sol(self, cand, n, sol_list):
        if len(cand) == 2 * n:
            return [cand]
        else:
            cand1 = cand + "("
            cand2 = cand + ")"
            cand1_safe = self.is_safe(cand1, n)
            cand2_safe = self.is_safe(cand2, n)
            # print(cand,"//",cand1,"//",cand2)
            if cand1_safe and cand2_safe:
                return sol_list + self.make_sol(cand1, n, sol_list) + self.make_sol(cand2, n, sol_list)
            elif cand1_safe:
                return sol_list + self.make_sol(cand1, n, sol_list)
            elif cand2_safe:
                return sol_list + self.make_sol(cand2, n, sol_list)