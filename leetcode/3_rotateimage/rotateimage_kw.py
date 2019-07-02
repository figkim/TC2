class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix[:] = [[matrix[n-1-j][i] for j in range(n)] for i in range(n)]
