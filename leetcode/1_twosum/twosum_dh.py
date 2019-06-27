class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_of_list = { val : idx for idx, val in enumerate(nums) }
        for i, v in enumerate(nums):
            if dict_of_list.get(target - v) is not None and i is not dict_of_list.get(target - v):
                return [i, dict_of_list.get(target - v)]
