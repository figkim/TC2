class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = None
        for i, j in enumerate(nums[::-1]):
            if i == 0:
                curr = j
            else:
                if j == curr:
                    nums.remove(j)
                else:
                    curr = j
        return len(nums)
