class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        if target < nums[start]:
            return 0
        if target > nums[end]:
            return len(nums)
        
        while start < end:
            middle = (start+end)//2
            
            if target > nums[middle]:
                start = middle + 1
            else:
                end = middle
                
        return start
