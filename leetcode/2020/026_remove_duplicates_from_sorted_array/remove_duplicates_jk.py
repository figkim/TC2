class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        
        for i in range(1, len(nums)):
            if nums[idx] < nums[i]:
                idx += 1
                nums[idx] = nums[i]
                
        return idx + 1
