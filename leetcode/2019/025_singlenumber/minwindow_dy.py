class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        checked = {}
        
        for num in nums:
            if num in checked:
                del checked[num]
                continue
            checked[num] = True
        return list(checked.keys())[0]