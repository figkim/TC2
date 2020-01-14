class Solution:
    def romanToInt(self, s: str) -> int:
        sym_dict = {
                        'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000
                    }
        
        res = 0
        for i, sym in enumerate(s):
            if i < len(s)-1 and sym_dict[sym] < sym_dict[s[i+1]]:
                res -= sym_dict[sym]
            else:
                res += sym_dict[sym]
        return res
