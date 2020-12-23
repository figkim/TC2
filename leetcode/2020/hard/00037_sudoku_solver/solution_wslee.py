# leetcode solution 참고... 넘모 어려운 것이에요
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        box_index = lambda row, col: (row // 3) * 3 + col // 3

        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue

                v = int(board[r][c])
                rows[r].add(v)
                cols[c].add(v)
                boxes[box_index(r, c)].add(v)

        def is_valid(r, c, v):
            condition = v not in rows[r] and v not in cols[c] and v not in boxes[box_index(r, c)]
            return condition

        def backtrack(r, c):
            if r == n - 1 and c == n:
                return True
            elif c == n:  # when reached the last column
                r += 1
                c = 0

            # current grid has been filled
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            for v in range(1, n + 1):
                if not is_valid(r, c, v):
                    continue
                else:
                    # if the valid condtion is satisfied
                    board[r][c] = str(v)
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[box_index(r, c)].add(v)

                    if backtrack(r, c + 1):
                        return True

                    # backtrack
                    board[r][c] = '.'
                    rows[r].remove(v)
                    cols[c].remove(v)
                    boxes[box_index(r, c)].remove(v)

            return False

        backtrack(0, 0)
