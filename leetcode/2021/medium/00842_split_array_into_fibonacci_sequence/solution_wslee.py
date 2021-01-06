class Solution:
    def splitIntoFibonacci(self, S):
        """
        솔루션 봐도 이해가 안 가서 Discuss 탭 참고했는데
        봐도 잘 모르겠음
        """
        n = len(S)
        if not n:
            return []
        ret = []
        max_num = 2 ** 31 - 1

        def dfs(idx, temp):
            if idx == n and len(temp) >= 3:
                ret.append(temp[:])
                return
            if len(temp) >= 2:
                next_num = temp[-2] + temp[-1]
                str_next_num = str(next_num)
                if next_num <= max_num and S[idx:].startswith(str_next_num):
                    temp.append(next_num)
                    dfs(idx + len(str_next_num), temp)
                    temp.pop()
            else:
                for i in range(idx + 1, n):
                    prefix = S[idx:i]
                    if prefix != '0' and prefix.startswith('0'):
                        continue
                    if int(prefix) <= max_num:
                        temp.append(int(prefix))
                        dfs(idx + len(prefix), temp)
                        temp.pop()

        dfs(0, [])
        return ret[0] if ret else []
