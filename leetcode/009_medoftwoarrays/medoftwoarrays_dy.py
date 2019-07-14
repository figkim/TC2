class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1 = 0 
        i2 = 0 
        ans = 0
        total_len = len(nums1) + len(nums2)
        for i in range(total_len):
            if i2 >= len(nums2) or (i1 < len(nums1) and nums1[i1] <= nums2[i2]):
                value = nums1[i1]
                i1 += 1
            else:
                value = nums2[i2]
                i2 += 1
                
            if total_len % 2 == 0:
                if i == total_len / 2:
                    ans += value
                    ans = ans/2
                    return ans 
                elif i == total_len / 2 - 1:
                    ans += value
            else:
                if i == total_len // 2:
                    return float(value)
                    
