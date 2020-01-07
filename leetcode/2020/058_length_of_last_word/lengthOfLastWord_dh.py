class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        metletter = False
        length = 0
        
        for i in s[::-1]:
            if i == ' ':
                if not metletter:
                    continue
                else:
                    return length
            else:
                metletter = True
                length += 1
            
        return length
                
