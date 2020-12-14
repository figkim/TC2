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

'''
with dynamic programming
class Solution:
    def trap(self, height: List[int]) -> int:
        left_list = []

        max_left = 0
        for num in height:
            max_left = max(max_left, num)
            left_list.append(max_left)


        right_list = []

        max_right = 0
        for num in height[::-1]:
            max_right = max(max_right, num)
            right_list.append(max_right)

        right_list.reverse()

        return sum([min(l, r) for l, r in zip(left_list, right_list)]) - sum(height)
'''
