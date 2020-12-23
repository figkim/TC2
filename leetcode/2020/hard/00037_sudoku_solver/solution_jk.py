# ref by https://dojinkimm.github.io/problem_solving/2019/10/16/boj-2580-sudoku.html
import copy

def vertical_check(i, n, board):
    for j in range(9):
        if board[i][j] != '.' and n == int(board[i][j]):
            return False
    return True

def horizontal_check(j, n, board):
    for i in range(9):
        if board[i][j] != '.' and n == int(board[i][j]):
            return False
    return True

def zone_check(k, n, board):
    x, y = divmod(k, 3)
    x *= 3
    y *= 3
    for i in range(3):
        for j in range(3):
            if board[x+i][y+j] != '.' and n == int(board[x+i][y+j]):
                return False
    return True

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        _board = copy.deepcopy(board)
        queue = [(0, _board)]
        
        zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == '.']

        while queue:
            index, _board = queue.pop()

            if index == len(zeros):
                print(_board)
                break

            for num in range(1, 10):
                i, j = zeros[index]
                k = 3*(i//3) + (j//3)
                if vertical_check(i, num, _board) and horizontal_check(j, num, _board) and zone_check(k, num, _board):
                    __board = copy.deepcopy(_board)
                    __board[i][j] = str(num)
                    queue.append((index+1, __board))

        for i in range(9):
            for j in range(9):
                board[i][j] = _board[i][j]
