class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        
        if (n < 4) or (n > 12):
            return None
        
        def split_into_4(k):
            a, b, c, d = [0,1,2],[0,1,2],[0,1,2],[0,1,2]
            
            possible = [[x+1,x+y+2,x+y+z+3,x+y+z+w+4] for x in a for y in b for z in c for w in d if x+y+z+w == k-4]
            
            return possible
        
        possible = split_into_4(n)
        
        if possible == []:
            return possible
        
        else:
            ans = list()
            for pos in possible:
                num1, num2, num3, num4 = (s[:pos[0]]), (s[pos[0]:pos[1]]), (s[pos[1]:pos[2]]), (s[pos[2]:])
                if (min(int(num1),int(num2),int(num3),int(num4)) >= 0) and (max(int(num1),int(num2),int(num3),int(num4)) <= 255) and (str(int(num1)) == num1) and (str(int(num2)) == num2) and (str(int(num3)) == num3) and (str(int(num4)) == num4):
                    ans.append((num1)+"."+(num2)+"."+(num3)+"."+(num4))
            return ans