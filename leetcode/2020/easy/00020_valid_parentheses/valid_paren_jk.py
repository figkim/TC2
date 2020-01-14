class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {'(':')', '{':'}', '[':']'}
        
        open_p = '({['
        
        hist = []
        
        for sym in s:
            if sym in open_p:
                hist.append(sym)
            else:
                if len(hist) == 0:
                    return False
                
                p = hist.pop()
                
                if sym != p_dict[p]:
                    return False
                
        return len(hist) == 0
