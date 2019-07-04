class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        if k > 0:
            return [max(nums[i:i+k]) for i in range(N - k + 1)]
        else:
            return []
