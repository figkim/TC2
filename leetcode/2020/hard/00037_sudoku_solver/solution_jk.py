import heapq

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        '''
        다른 사람 정답을 참고했습니다. 따라서 밑에 답에 대한 설명을 적습니다.
        
        기본적인 아이디어 : backtracking을 통해 가능한 경우를 모두 탐색한다.
        이 답안의 경우 빈 칸에 들어갈 수 있는 후보군을 관리하고 heap을 이용하여 가장 후보군이 적은 칸부터 채워나가 빠르게 답을 찾을 수 있다.
        후보군 관리는 set을 통해 이루어지며, row, col, zone(3x3) 별로 각각 관리하고 빈칸은 이들의 교집합을 통해 후보 숫자를 관리한다.        
        heap에는 빈칸의 후보군 수를 통해 정렬되고, 좌표값이 저장된다.
        
        backtracking 시 heap을 통해 가장 후보군의 수가 적은 것부터 시도를 하며 recursive하게 다음 스텝을 탐색해나간다.
        모든 빈칸이 채워지게 되면 True를 리턴하게 되는데 이 값을 받아서 현재 시도한 빈칸의 값이 맞는지 확인한다.
        
        다른 답안의 경우 빈칸에 1부터 9까지의 모든 경우를 시도하게 되며, 좌표값의 순서대로 시도를 하기 때문에 매우 비효율적이나,
        이 방식의 경우 후보군의 수가 적은대로 시도한다는 점과 후보군만 시도한다는 점에서 매우 효율적인 방법이다.
        
        '''
        
        
        row_candi = [set([str(c) for c in range(1, 10)]) for _ in range(9)]
        col_candi = [set([str(c) for c in range(1, 10)]) for _ in range(9)]
        zone_candi = [set([str(c) for c in range(1, 10)]) for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                num = board[i][j]
                row_candi[i].remove(num)
                col_candi[j].remove(num)
                k = 3*(i//3) + (j//3)
                zone_candi[k].remove(num)

        min_heap = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.': continue
                k = 3*(i//3) + (j//3)
                candi = row_candi[i].intersection(col_candi[j]).intersection(zone_candi[k])

                heapq.heappush(min_heap, [len(candi), i, j, k])

        def solve():
            if not min_heap: return True
            _, i, j, k = heapq.heappop(min_heap)

            candi = row_candi[i].intersection(col_candi[j]).intersection(zone_candi[k])

            for num in candi:
                board[i][j] = str(num)
                row_candi[i].remove(num)
                col_candi[j].remove(num)
                zone_candi[k].remove(num)
                if solve(): return True

                row_candi[i].add(num)
                col_candi[j].add(num)
                zone_candi[k].add(num)

            board[i][j] = '.'
            heapq.heappush(min_heap, [len(candi), i, j, k])
            return False

        solve()
