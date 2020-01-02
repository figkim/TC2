class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if len(matrix) == 0:
            return list()
        
        num_row, num_col = len(matrix), len(matrix[0])
        output = list()
        
        def peeling(output,matrix,num_row,num_col):            
            output.extend(matrix[0])
            matrix.pop(0)
            num_row -= 1
            for i in range(0,len(matrix)):
                output.append(matrix[i][-1])
                matrix[i].pop(-1)
            num_col -= 1
            output.extend(matrix[-1][::-1])
            matrix.pop(-1)
            num_row -= 1
            for i in range(len(matrix)-1,-1,-1):
                output.append(matrix[i][0])
                matrix[i].pop(0)
            num_col -= 1
            return output, matrix ,num_row, num_col
        
        while (num_row > 1) and (num_col > 1):
            output, matrix, num_row, num_col = peeling(output,matrix,num_row,num_col)
        if num_row == 1:
            output.extend(matrix[0])
        elif num_col == 1:
            for row in matrix:
                output.append(row[0])
            
        return output