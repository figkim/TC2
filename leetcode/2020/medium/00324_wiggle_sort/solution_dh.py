class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            pass
        else:
            nums.sort()
            temp = nums.copy()
            idx = len(nums) // 2 + len(nums) % 2

            for i in range(idx - 1):
                nums[2 * i], nums[2 * i + 1] = temp[idx - (i + 1)], temp[-(i + 1)]

            if len(nums) % 2 == 0:
                nums[-2], nums[-1] = temp[0], temp[idx]
            else:
                nums[-1] = temp[0]
