class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while True:
            if i >= len(nums):
                break
            if nums[i] == nums[i-1]:
                nums[i:] = nums[i+1:]
            else:
                i += 1
        return len(nums)
