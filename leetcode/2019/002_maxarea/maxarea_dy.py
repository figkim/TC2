class Solution:
    def maxArea(self, height: List[int]) -> int:
        get_container = lambda i, j: min(height[i], height[j]) * abs(j-i)
        
        left_end = 0
        right_end = len(height) - 1
        
        max_container = 0
        
        while left_end <= right_end:
            container = get_container(left_end, right_end) 
            max_container = max(max_container, container)
            
            if height[left_end] >= height[right_end]:
                right_end -= 1
            else:
                left_end += 1
            
        return max_container
