class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        new_dict = dict()
        prev_itr = N - 1
        prev_num = nums[prev_itr]
        for curr_itr in reversed(range(N - 1)):
            if prev_num not in new_dict:
                new_dict[prev_num] = prev_itr
            curr_num = nums[curr_itr]
            new_dict = dict(sorted(new_dict.items()))
            for key in new_dict:
                if key > curr_num:
                    target_itr = new_dict[key]
                    nums[curr_itr] = key
                    nums[target_itr] = curr_num
                    nums[curr_itr + 1:] = nums[curr_itr + 1:][::-1]
                    # nums[curr_itr+1:] = sorted(nums[curr_itr+1:])
                    return nums
            else:
                prev_itr = curr_itr
                prev_num = curr_num

        nums[:] = nums[::-1]
        return nums