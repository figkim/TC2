class Solution(object):
    def maxSubArray(self, nums):
        dp = nums[0]
        maxval = dp
        for itr, i in enumerate(nums[1:]):
            dp = max(dp, 0) + i
            maxval = max(maxval, dp)
        return maxval
