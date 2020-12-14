class Solution:
    def trap(self, height: List[int]) -> int:
        if height:
            ans = 0
            left_max = [0] * len(height)
            right_max = [0] * len(height)
            left_max[0] = height[0]
            right_max[-1] = height[-1]
            for i in range(1, len(height)):
                # print(len(left_max), len(height), i)
                left_max[i] = max(left_max[ i -1], height[i])
            for i in range(len(height ) -2, -1, -1):
                # print(len(right_max), len(height), i)
                right_max[i] = max(right_max[ i +1], height[i])

            for i in range(len(height)):
                ans += min(left_max[i], right_max[i]) - height[i]
                # print(i, left_max, right_max, ans)
        else:
            ans = 0

        return ans
