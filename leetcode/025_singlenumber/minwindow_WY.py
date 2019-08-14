class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        # sol1
        nums.sort()
        count = 0
        
        while count < len(nums):
            #print count, nums
            if (count+1 < len(nums)) and (nums[count] == nums[count+1]):
                count += 2
            else:
                return nums[count]
        """


        # sol 2
        return sum(set(nums))*2 - sum(nums)