class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        half_idx = (len(nums) + 1)//2
        nums[0::2] = sorted_nums[:half_idx][::-1]
        nums[1::2] = sorted_nums[half_idx:][::-1]