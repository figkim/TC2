class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        two_cnt = 0
        
        i = 0
        cnt = 0
        
        while cnt < n:
            cnt += 1
            if nums[i] == 0:
                i += 1
            elif nums[i] == 1:
                nums[:] = nums[:i] + nums[i+1:]
                nums.append(1)
            elif nums[i] == 2:
                nums[:] = nums[:i] + nums[i+1:]
                two_cnt += 1
                
        for _ in range(two_cnt):
            nums.append(2)
