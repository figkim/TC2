import copy
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i, mem in enumerate(copy.deepcopy(matrix)):
            for j, ent in enumerate(mem):
                matrix[j][n - i - 1] = ent