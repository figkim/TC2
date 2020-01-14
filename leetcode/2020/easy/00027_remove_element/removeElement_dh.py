class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                del nums[idx]
            else:
                idx += 1
        return len(nums)
