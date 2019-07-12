class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0        
        i = 0
        j = len(height) - 1
        
        while i < j:
            h1 = height[i]
            h2 = height[j]
            
            if h1 < h2:
                max_area = max(max_area, h1 * (j - i))
                i += 1
                
            else:
                max_area = max(max_area, h2 * (j - i))
                j -= 1
                
        return max_area
