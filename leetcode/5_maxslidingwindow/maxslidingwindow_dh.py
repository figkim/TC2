class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if nums:
            return [max(nums[i:i + k]) for i in range(len(nums)-k+1)]
        else:
            return []