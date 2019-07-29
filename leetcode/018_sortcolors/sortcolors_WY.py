class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[:] = [0]*nums.count(0) + [1]*nums.count(1) + [2]*nums.count(2)