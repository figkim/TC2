class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        lcp = strs[0]
        for string in strs:
            if lcp == "":
                return lcp
            if len(lcp) > len(string):
                lcp = lcp[:len(string)]
            for i in range(min(len(string), len(lcp))):
                if string[i] == lcp[i]:
                    continue
                else:
                    lcp = lcp[:i]
                    break
        return lcp
