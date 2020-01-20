class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = set()
        s = 0
        
        for num in nums:
            if num not in tmp:
                tmp.add(num)
                s += num
                
            else:
                s -= num
                
        return s
