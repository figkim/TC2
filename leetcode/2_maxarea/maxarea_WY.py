class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # naive O(n^2)-approach occurs runtime error...
        
        max_val = 0
        start, end = 0, len(height)-1
        
        while start < end:
            
            if height[start] > height[end]:
                area = (end - start) * height[end]
                end -= 1
            # We don't have to search for "start" values in interval (start,end) since the area will be always smaller than the current area, hence search end-1 in the next step.
                
            else:
                area = (end - start) * height[start]
                start += 1
            # We don't have to search for "end" values in interval (start,end) since the area will be always smaller than the current area, hence search start+1 in the next step.
            
            if max_val < area:
                max_val = area
                
        return max_val
