class Solution(object):
    def check_components_are_identical(self, lst):
        for i in lst[1:]:
            if i != lst[0]:
                return False
        return True
    
    def longestCommonPrefix(self, strs):
        pref = ""
        if len(strs)==0:
            return pref
        elif len(strs)==1:
            return strs[0]
        else:
            minlen = min(list(map(len, strs)))
            if minlen == 0:
                return pref
            else:
                for i in range(minlen):
                    prefx = list(map(lambda x: x[:i+1], strs))
                    if self.check_components_are_identical(prefx):
                        pref = prefx[0]
                    else:
                        return pref
                return pref
