class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        score_list = [1] + [0] * len(t)

        n = len(t)
        
        # let f(t, s) : number of distinct target t in source s
        #
        # if f(t[:i-1], s[:j-1]) = n1 and f(t[:i], s[:j-1]) = n2
        # then f(t[:i], s[:j]) = n1 + n2 (if t[i] == s[j]) or = n2 (otherwise)
        # 
        # so we can construct the distinct matrix by dynamic programming (which is first try)
        #
        # we don't have to hold whole matrix, instead of holding the current(jth column)
        # because, n2 must be calculated the previous step
        # But we need to consider repeated char like ra'bb'it
        # so reversewise counting is needed to consider that case

        for c1 in s:
            if c1 in t:
                for i in range(n, 0, -1):
                    c2 = t[i-1]
                    if c1 == c2:
                        score_list[i] += score_list[i - 1]
                        
        return score_list[-1]
