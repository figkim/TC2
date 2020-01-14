class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i,n in enumerate(nums):
            cand = target-n
            if cand in d:
                return [d[cand],i]
            else:
                d[n] = i