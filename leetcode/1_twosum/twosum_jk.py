class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i, num in enumerate(nums):
            if num in new_dict:
                return (i, new_dict[num])
            rest = target - num
            new_dict[rest] = i
