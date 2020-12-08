class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        N = len(nums)
        new_nums = sorted(nums, reverse=True)
        
        for i in range(N//2):
            nums[2*i] = new_nums[i+N//2]
            nums[2*i+1] = new_nums[i]
            
        if N%2:
            nums[-1] = new_nums[-1]
            
        # the better code from other code
        #
        # N = len(nums)
        # nums.sort()
        # nums[::2], nums[1::2] = nums[N//2:], nums[:N//2]
        
