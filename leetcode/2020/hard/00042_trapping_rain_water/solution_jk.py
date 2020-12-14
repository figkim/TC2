class Solution:
    def trap(self, height: List[int]) -> int:
        # solution의 two point를 참고하였습니다. (넘나 어려운 것.. ㅠㅠㅠ)
        
        left = 0
        right = len(height) - 1
        
        max_left = 0
        max_right = 0
        
        ans = 0

        while left < right:

            if height[left] < height[right]:
                if max_left > height[left]:
                    ans += max_left - height[left]
                else:
                    max_left = height[left]
                    
                left += 1
                
            else:
                if max_right > height[right]:
                    ans += max_right - height[right]
                else:
                    max_right = height[right]
                    
                right -= 1

        return ans
