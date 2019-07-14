class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        vert_m = [[0]*len(matrix[0]) for i in range(len(matrix))] # longest vertical line included (i,j)
        hor_m = [[0]*len(matrix[0]) for i in range(len(matrix))] # longest horizontal line included (i,j)
        len_m = [[0]*len(matrix[0]) for i in range(len(matrix))] # length for square included (i,j)
        ans = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    vert_m[i][j] = vert_m[i-1][j] + 1 if i >= 0 else 1
                    hor_m[i][j] = hor_m[i][j-1] + 1 if j >= 0 else 1
                    length = min(vert_m[i][j], hor_m[i][j])
                    len_m[i][j] = len_m[i-1][j-1]+1 if (length-1) >= len_m[i-1][j-1] else length
                    
                    if len_m[i][j] * len_m[i][j] > ans:
                        ans = len_m[i][j] * len_m[i][j]
        return ans
