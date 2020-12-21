class Solution:
    def maximumSwap(self, num: int) -> int:
        s_num = list(str(num))
        N = len(s_num)

        for i in range(N-1):
            curr_num = s_num[i]
            j, max_num = max(enumerate(s_num[::-1][:N-i-1], 1), key=lambda x:x[1])
            j = N - j

            if i != j and s_num[i] < s_num[j]:
                s_num[i], s_num[j] = s_num[j], s_num[i]
                return int(''.join(s_num))

        return int(''.join(s_num))    
