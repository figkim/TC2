class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        '''
        다른 사람의 코드를 봐서 역시 설명을 추가합니다.
        
        기존에는 가장 작은 것들을 찾아서 했는데, 사실 다 필요없고, 조건만 맞추면 됩니다.
        row와 col 중에 작은 것을 찾아서 써 넣고, 아닌 쪽에서 뺴주면 됩니다.
        
        왜 이 생각을 못했찌...? 가장 작은 것들부터 찾아야 한다는 생각에 빠져서.. ㅠㅠ
        하지만 heapq과 큰 차이가 없네..
        '''
        N, M = len(rowSum), len(colSum)

        answer = [[0 for _ in range(M)] for _ in range(N)]

        i, j = 0, 0

        while i < N and j < M:
            row, col = rowSum[i], colSum[j]

            if row < col:
                answer[i][j] = row
                colSum[j] -= row
                i += 1
            elif row > col:
                answer[i][j] = col
                rowSum[i] -= col
                j += 1
            else:
                answer[i][j] = row
                i += 1
                j += 1

        return answer
