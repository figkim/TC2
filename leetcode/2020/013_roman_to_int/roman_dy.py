class Solution:
    def romanToInt(self, s: str) -> int:
        values = dict(zip("IVXLCDM", [1,5,10,50,100,500,1000]))
        
        flag = False
        ret_value = 0
        
        for i in range(len(s)):
            if flag:
                flag = False
                continue
                
            if values[s[i]] % 10 <= 1 and i < len(s) - 1:
                check = values[s[i+1]] / values[s[i]]
                if check == 5 or check == 10:
                    ret_value += values[s[i+1]]-values[s[i]]
                    flag = True
                else:
                    pass
            if not flag:
                ret_value += values[s[i]]
        return ret_value
                
            
        
        
        
