import copy
class Solution(object):
    def rotate(self, matrix):
        """
        in list-memory perspective, rotate function just re-arrange
        the order of memory. Refer to the symbols allocated to each
        number. You can easily find the pattern `rotate --> matrix[j][n - i - 1]`

        matrix      -->     rotated matrix
        [0] |1|*                [0] |7|@
            |2|*                    |4|$
            |3|*                    |1|*
        [1] |4|$                [1] |8|@
            |5|$                    |5|$
            |6|$                    |2|*
        [2] |7|@                [2] |9|@
            |8|@                    |6|$
            |9|@                    |3|*

        """
        n = len(matrix)
        for i, mem in enumerate(copy.deepcopy(matrix)):
            for j, ent in enumerate(mem):
                matrix[j][n - i - 1] = ent