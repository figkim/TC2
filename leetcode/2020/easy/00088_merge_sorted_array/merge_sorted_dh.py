class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i, j in enumerate(nums1):
            if not nums2:
                nums1[m+n:] = nums2
                return
            else j > nums2[0]:
                nums1[i+1:] = nums1[i:]
                nums1[i] = nums2.pop(0)
        if nums2:
            nums1[m+n-len(nums2):] = nums2
