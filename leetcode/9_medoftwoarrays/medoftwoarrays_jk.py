class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = sorted(nums1 + nums2)
        
        n =len(new_nums) 
        if n % 2 == 1:
            return new_nums[n//2]
        else:
            return sum(new_nums[n//2-1:n//2+1])/2
