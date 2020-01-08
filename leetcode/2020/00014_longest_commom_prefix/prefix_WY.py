class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            min_len = 1e+16

            for i,string in enumerate(strs):
                if len(string) < min_len:
                    min_len = len(string)
                    index = i

            shortest = strs.pop(index)
            print(shortest)
            if len(shortest) == 0:
                return ""
            else:
                longest = ""

                for k in range(1,len(shortest)+1):
                    boolean = True
                    for string in strs:
                        if shortest[:k] != string[:k]:
                            boolean = False
                            break
                    if boolean and k > len(longest):
                        longest = shortest[:k]

                return longest