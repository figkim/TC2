class Solution(object):
   def increasingTriplet(self, nums):
       """
       :type nums: List[int]
       :rtype: bool
       """

       if len(nums) < 3:
           return False

       left, mid = max(nums)+1, max(nums)+1

       for n in nums:
           if n <= left:
               left = n
           elif n <= mid:
               mid = n
           else:
               return True

       return False