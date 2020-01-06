class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        if len(nums) < 2:
            return len(nums)
        else:
            while count < len(nums) - 1:
                if nums[count] == nums[count+1]:
                    nums.pop(count+1)
                else:
                    count += 1
            return count + 1

