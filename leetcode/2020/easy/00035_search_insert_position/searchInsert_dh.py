class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        idx = 0
        while idx < len(nums) and nums[idx] < target:
            idx += 1
        return idx
