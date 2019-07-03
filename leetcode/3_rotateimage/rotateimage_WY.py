class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = map(list,zip(*matrix[::-1]))

        # *matrix : unpack and put together i'th elements of lists in matrix
        # [::-1] : extract lists in matrix in reverse order
        # map(list,~) : convert tuples to list

        # matrix = [[1,2,3],[4,5,6],[7,8,9]]
        # zip(*matrix) = (1,4,7) (2,5,8) (3,6,9) (returns three iterable tuples)
        # zip(*matrix[::-1]) = (7,4,1) (8,5,2) (9,6,3)
        # map(list,~) converts tuples to list
        # result matrix = [[7,4,1],[8,5,2],[9,6,3]]
        