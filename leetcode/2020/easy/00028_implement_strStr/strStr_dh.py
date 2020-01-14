class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        checker = False
        if needle == '':
            return 0
        
        for idx_hay, i in enumerate(haystack):
            if i == needle[0] and (len(haystack) >= idx_hay + len(needle)):
                for idx_nee, j in enumerate(needle):
                    if haystack[idx_hay + idx_nee] != needle[idx_nee]:
                        break
                    if idx_nee == len(needle)-1:
                        return idx_hay
        return -1
