class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mem = [[1] * (len(s) + 1)]
        [mem.append([0]*(len(s)+1)) for i in range(len(t))]
        for i in range(len(t)):
            for j in range(len(s)):
                mem[i+1][j+1] = mem[i+1][j]
                mem[i+1][j+1] += mem[i][j] if t[i] == s[j] else 0
        
        return mem[len(t)][len(s)]

        
