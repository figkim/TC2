class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        
        # easy sort method
        
        nums = nums1+nums2
        nums.sort()
        
        if len(nums)%2 == 0:
            return sum(nums[len(nums)/2 - 1:len(nums)/2 + 1])*0.5
        else:
            return nums[len(nums)/2]
        
        """
        # are there any faster ways?
        # suppose nums2 is longer
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        nums1_med_idx, nums2_med_idx = (len(nums1)+1)//2 - 1, (len(nums2)+1)//2 - 1
        
        """