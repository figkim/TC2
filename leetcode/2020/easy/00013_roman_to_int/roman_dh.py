class Solution(object):
    dict_romans = {"I": 1, 
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000}
    
    def romanToInt(self, s):
        sum = 0
        for i, l in enumerate(s):
            if (i != len(s) - 1) and ((l == "I" and s[i+1] in ["V", "X"]) or (l == "X" and s[i+1] in ["L", "C"]) or (l == "C" and s[i+1] in ["D", "M"])):
                sum -= self.dict_romans[l]    
            else:    
                sum += self.dict_romans[l]
        return sum
        
