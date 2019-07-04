class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # initiailize dp-table as dp_table
        # (j+1)-th element of dp_table implies "the number of expression upto t[j]"
        dp_table = [1] + [0] * len(t)
        
        # run dp and when t[j] is equal to some s[i], add "the number of expression upto t[j-1]" to "the number of expression upto t[j]"
        for i in range(len(s)):
            for j in range(min(i+1,len(t)),0,-1):
                # here, the reason for the reverse itertaion is for the case such as t="rabbit"
                # 일단 현재까지 t-substiring의 끝자리가 s-substring에서 같은게 나와야 dp-table을 누적해서 더하는게 의미가 있는것이고, 그렇기 때문에 역순으로 iteration 진행
                # 만약 정순으로 iteration 진행하면 summation 하다가 현재 t-substring의 끝자리가 s-substring과 같은게 안나올 수 있어서 dp-table에서 괜히 엄한 값을 더해버리는 일이 발생
                if s[i] == t[j-1]:
                    dp_table[j] += dp_table[j-1]
        
        return dp_table[-1]
