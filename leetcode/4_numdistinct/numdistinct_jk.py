class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # First try:
        n = len(s) + 1
        m = len(t) + 1

        score_board = [[1] * n for _ in range(m)]

        for i in range(1, m):
            score_board[i][0] = 0

        for i, c1 in enumerate(t, 1):
            for j, c2 in enumerate(s, 1):
                if c1 == c2:
                    score_board[i][j] = score_board[i][j-1] + score_board[i-1][j-1]
                else:
                    score_board[i][j] = score_board[i][j-1]
        
        return score_board[-1][-1]
