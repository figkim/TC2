class ContinueI(Exception):
    pass

class Solution(object):
    def matchSquare(self, matrix, size, r, c):
        submat =[i[c:c+size] for i in matrix[r:r+size]]
        if sum([sum(i) for i in submat]) == size**2:
            return True
        else:
            return False

    def convertStringtoInt(self, matrix):
        tempmat = matrix
        for i, r in enumerate(tempmat):
            matrix[i] = map(int, r)
        return tempmat

    def maximalSquare(self, matrix):
        continue_i = ContinueI()
        curmax = 1
        matrix = self.convertStringtoInt(matrix)
        if not sum([sum(i) for i in matrix]): # zero matrix
            return 0
        else:
            for s in range(2, min(len(matrix), len(matrix[0])) + 1):
                try:
                    for r in range(len(matrix) - (s-1)):
                        for c in range(len(matrix[0]) - (s-1)):
                            if self.matchSquare(matrix, s, r, c):
                                curmax = s**2
                                raise continue_i
                except ContinueI:
                    continue
            return curmax