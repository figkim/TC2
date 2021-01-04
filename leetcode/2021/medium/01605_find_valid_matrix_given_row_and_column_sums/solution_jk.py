import heapq

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        '''
        다른 사람의 코드를 참고하여 수정하여 기본 아이디어를 쓰겠습니다.
        
        기존 코드에서는 매번 rowSum과 colSum에서 0보다 큰 것 중에서 최소값을 찾느라 시간이 오래 걸렸습니다.
        그래서 이 부분을 heap queue로 바꿔서 시간을 단축하였습니다.
        
        다른 부분은 다 동일하고, 가장 작은 숫자를 찾는데에만 heap queue 로 바꿨습니다
        그리고 0인 부분은 추가하지 않아서 별도의 조건문이 필요 없습니다.
        '''
        N, M = len(rowSum), len(colSum)

        row_heap = [[num, i] for i, num in enumerate(rowSum)]
        col_heap = [[num, j] for j, num in enumerate(colSum)]
        
        heapq.heapify(row_heap)
        heapq.heapify(col_heap)

        answer = [[0 for _ in range(M)] for _ in range(N)]

        while row_heap or col_heap:
            row_min, i = heapq.heappop(row_heap)
            col_min, j = heapq.heappop(col_heap)

            min_num = min(row_min, col_min)
            answer[i][j] = min_num

            if row_min > min_num:        
                heapq.heappush(row_heap, [row_min - min_num, i])

            if col_min > min_num:        
                heapq.heappush(col_heap, [col_min - min_num, j])

        return answer
