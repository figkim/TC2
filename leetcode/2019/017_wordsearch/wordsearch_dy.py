class Solution:
    def get_loc(self, loc, direc):
        new_loc = [loc[0] + direc[0], loc[1]+direc[1]]

        if new_loc[0] < 0 or new_loc[1] < 0 or new_loc[0] >= len(self.board) or new_loc[1] >= len(self.board[0]):
            return None
        return new_loc

    def check(self, loc, visited, word):
        if len(word) == len(self.word):
            return True
        visited[loc[0]][loc[1]] = 1
        checked = False

        for direc in self.compass:
            new_loc = self.get_loc(loc, direc)

            if new_loc is None or visited[new_loc[0]][new_loc[1]] == 1:
                continue

            curr_char = self.board[new_loc[0]][new_loc[1]]
            if self.word[len(word)] == curr_char:
                checked = checked or self.check(new_loc, visited, word+curr_char)
        visited[loc[0]][loc[1]] = 0
        return checked

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word

        self.compass = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        checked = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_char = self.board[i][j]
                if self.word[0] == curr_char:
                    visited = [[0]*len(board[0]) for _ in range(len(board))]
                    checked = checked or self.check([i,j], visited, curr_char)

        return checked


