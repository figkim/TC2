class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        score_list = [1] + [0] * len(t)

        n = len(t)

        for c1 in s:
            if c1 in t:
                for i in range(n, 0, -1):
                    c2 = t[i-1]
                    if c1 == c2:
                        score_list[i] += score_list[i - 1]
                        
        return score_list[-1]
