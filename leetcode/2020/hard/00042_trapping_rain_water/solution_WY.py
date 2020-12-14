class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = [0]*n, [0]*n
        for i in range(n):
            if i == 0:
                left[i] = height[i]
                right[-(i+1)] = height[-(i+1)]
            else:
                left[i] = max(left[i-1],height[i])
                right[-(i+1)] = max(right[-i],height[-(i+1)])
        count = 0
        for i in range(1,n-1):
            count += min(left[i], right[i]) - height[i]
        return count