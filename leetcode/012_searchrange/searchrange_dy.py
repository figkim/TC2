class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            first = nums.index(target)
        except:
            first = end = -1
        if first != -1:
            nums.reverse()
            end = len(nums) - nums.index(target) - 1
        return [first, end]
