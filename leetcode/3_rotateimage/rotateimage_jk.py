class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        '''
        2nd try
        
        matrix[::] = [row[::-1] for row in zip(*matrix)]
        
        [A B]
        [C D]
        
        (NW flip)
        
        [A C]
        [B D]
        
        (W flip)
        
        [C A]
        [D B]        
        '''

        n = len(matrix)

        # In case of n is odd number
        # In this case, matrix can be splited by 5 pieces
        # [0, 1, 2]      [0, 1] |[2]
        # [3, 4, 5]  =>  [3]|[4]|[5]
        # [6, 7, 8]      [6]| [7, 8]
        #
        # width, height are size of 4 pieces except the center one
        if n % 2 == 1:
            half = n // 2
            width = half
            height = half + 1
            
        # In case of n is even number
        # In this case, matrix can be splited by 4 pieces with same size
        # [ 0,  1,  2,  3]    [ 0,  1] [2, 3]
        # [ 4,  5,  6,  7] => [ 4,  5] [6, 7]
        # [ 8,  9, 10, 11]    [ 8,  9] [10, 11]
        # [12, 13, 14, 15]    [12, 13] [14, 15]
        #
        # width, height are size of 4 peices
        else:
            half = (n - 1) / 2
            width = n//2
            height = n//2

        # Use rotation formula
        # first move the each indices to coordinate
        # second shift each indices to make their center zero
        # third apply rotation fomula
        # last shift to original position
        
        # ex. if n is 3 (half is 1.5)
        # [j][i] = (0, 0) -> (-1.5, 1.5) -> (1.5, -1.5) -> (3, 0) (j : row, i : column)
        #
        # prev : the value to replace
        # temp : the value to be replace
        for i in range(width):
            for j in range(height):
                prev = matrix[i][j]
                for _ in range(4):
                    i, j = j, int(- i + 2 * half)
                    temp = matrix[i][j]
                    matrix[i][j] = prev
                    prev = temp
