from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if t == "":
            return ""
        
        min_len = len(s)+1
        min_str = ""
        start, end = 0, len(t) - 1
        
        t_counter = Counter(t)
        s_counter = Counter(s[start:end])
        
        while (end < len(s)):
            s_counter[s[end]] += 1
            while (start <= end) and self.check(s_counter,t_counter):
                if min_len > end - start:
                    min_len = end - start
                    min_str = s[start:end+1]
                else:
                    pass
                s_counter[s[start]] -= 1
                start += 1
            end += 1
        
        return min_str if min_len <= len(s) else ""
        
    def check(self,s_counter,t_counter):
        boolean = False
        for key,value in t_counter.iteritems():
            if s_counter[key] >= value:
                boolean = True
            else:
                return False
        return boolean
            