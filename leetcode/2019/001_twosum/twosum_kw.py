class Solution:
    def twoSum(self,nums, target):
        N = len(nums)
        check_dict = {}
        for itr1 in range(N):
            num1 = nums[itr1]
            difference = target - num1
            if difference in check_dict:
                itr2 = check_dict[difference]
                return [itr2,itr1]
            else:
                check_dict[num1] = itr1