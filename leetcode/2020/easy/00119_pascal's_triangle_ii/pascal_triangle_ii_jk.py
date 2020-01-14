class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = [1]
        
        for n in range(1, rowIndex+1):
            tri = [1] + [a+b for a, b in zip(tri[:-1], tri[1:])] + [1]
            
        return tri
