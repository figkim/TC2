class Solution:
    def checkFinish(self, matrix, result):
        return len(matrix) * len(matrix[0]) == len(result)
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        result = []
        while True:
            for i in range(left, right+1):
               result.append(matrix[top][i])
            top += 1
            if self.checkFinish(matrix, result):
                return result
            
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            if self.checkFinish(matrix, result):
                return result
            
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            if self.checkFinish(matrix, result):
                return result
            
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1
            if self.checkFinish(matrix, result):
                return result
            