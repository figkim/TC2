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

        if n % 2 == 1:
            half = n // 2
            width = half
            height = half + 1
            
        else:
            half = (n - 1) / 2
            width = n//2
            height = n//2
        for i in range(width):
            for j in range(height):
                prev = matrix[i][j]
                for _ in range(4):
                    i, j = j, int(- i + 2 * half)
                    temp = matrix[i][j]
                    matrix[i][j] = prev
                    prev = temp
