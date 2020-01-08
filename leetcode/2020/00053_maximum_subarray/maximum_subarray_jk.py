class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = 0
        max_num = nums[0]
        
        for i, num in enumerate(nums):
            dp = max(num, num + dp)
            max_num = max(max_num, dp)
            
        return max_num
