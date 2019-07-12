class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for idx, val in enumerate(nums):
            remain = target - val
            if remain in checked:
                return [checked[remain], idx]
            checked[val] = idx
