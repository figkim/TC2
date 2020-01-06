class Solution:
    def countAndSay(self, n: int) -> str:
        seq = '1'
        
        for _ in range(n-1):
            s = ''

            idx = 0
            num = ''
            leng = 0

            while idx < len(seq):
                if num == seq[idx]:
                    leng += 1
                else:
                    s += str(leng) + num
                    num = seq[idx]
                    leng = 1

                idx += 1

            s += str(leng) + num
            seq = s[1:]

        return seq
