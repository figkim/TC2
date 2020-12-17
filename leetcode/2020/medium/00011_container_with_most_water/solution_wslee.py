class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if area > res:
                res = area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res

#         brute-force solution (not accepted)
# for i in range(len(height)-1):
#     for j in range(i+1, len(height)):
#         w = abs(i-j)
#         h = min(height[i], height[j])
#         area = w * h
#         print(i,j, w,h,area)
#         if area > res:
#             res = area
# return res
