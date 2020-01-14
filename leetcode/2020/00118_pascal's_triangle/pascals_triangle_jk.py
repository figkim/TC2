class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        
        result = [[1]]
        
        for n in range(2, numRows+1):
            tmp = [1] + [a+b for (a, b) in zip(result[-1][:-1], result[-1][1:])] + [1]
            result.append(tmp)
            
        return result
