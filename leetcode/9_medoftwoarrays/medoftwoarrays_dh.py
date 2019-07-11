class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nlist = nums1+nums2
        nlist.sort()
        point, edge = len(nlist) / 2, len(nlist) % 2
        if edge:
            return float(nlist[point])
        else:
            return float(nlist[point-1] + nlist[point])/2