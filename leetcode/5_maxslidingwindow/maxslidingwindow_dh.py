class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        temp = []
        for i in range(len(nums) - k + 1):
            temp.append(max(nums[i:i + k]))
        return temp