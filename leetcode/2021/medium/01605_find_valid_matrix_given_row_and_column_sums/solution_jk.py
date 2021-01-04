class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N, M = len(rowSum), len(colSum)

        answer = [[0 for _ in range(M)] for _ in range(N)]

        while sum(rowSum) > 0 or sum(colSum) > 0:
            i, row_min = min(filter(lambda x:x[1]>0, enumerate(rowSum)), key=lambda x:x[1])
            j, col_min = min(filter(lambda x:x[1]>0, enumerate(colSum)), key=lambda x:x[1])
            
            min_num = min(row_min, col_min)

            answer[i][j] = min_num
            rowSum[i] -= min_num
            colSum[j] -= min_num

        return answer
