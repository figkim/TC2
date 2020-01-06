class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while True:
            if len(nums) <= i:
                break
            if nums[i] == val:
                nums[i:] = nums[i+1:]
            else:
                i+=1
        return len(nums)
