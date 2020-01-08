class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        cnt = 0
        curr = nums[0]
        for i, j in enumerate(nums[1:]):
            if j == curr:
                del nums[i-cnt]
                cnt += 1
            else:
                curr = j
        return len(nums)
