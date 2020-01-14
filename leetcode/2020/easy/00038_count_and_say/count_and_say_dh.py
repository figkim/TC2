class Solution(object):
    def convert_count(self, input, cnt):
        return str(cnt) + input
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        
        idx = 1
        cnt = 1
        temp = self.countAndSay(n-1)
        curr = temp[0]
        word = ''
        
        for i, let in enumerate(temp[1:]):
            if curr != let:
                word += self.convert_count(curr, cnt)
                cnt = 1
                curr = let
            else:
                cnt += 1
            if i == len(temp[1:]) - 1:
                word += self.convert_count(curr, cnt)
        
        return word
