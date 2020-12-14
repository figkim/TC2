class Solution:
    def trap(self, height: List[int]) -> int:
        # solution의 two point를 참고하였습니다. (넘나 어려운 것.. ㅠㅠㅠ)
        
        left = 0
        right = len(height) - 1

        ans = 0

        while left < right:
            m_h = min(height[left], height[right])

            if height[left] < height[right]:
                left += 1        

                while left < right and m_h > height[left]:
                    ans += max(m_h - height[left], 0)
                    left += 1

            else:
                right -= 1

                while left < right and m_h > height[right]:
                    ans += max(m_h - height[right], 0)
                    right -= 1


        return ans
