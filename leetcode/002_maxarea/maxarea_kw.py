class Solution(object):
    def maxArea(self, height):
        # O(N)
        N = len(height)
        itr1 = 0
        itr2 = N-1
        left = height[itr1]
        right = height[itr2]
        sol = min(left,right)*(itr2-itr1)
        while itr1 < itr2:
            left = height[itr1]
            right = height[itr2]
            if left > right:
                itr2 -= 1
            else:
                itr1 +=1
            sol = max(sol,min(height[itr1],height[itr2])*(itr2-itr1))
        return sol