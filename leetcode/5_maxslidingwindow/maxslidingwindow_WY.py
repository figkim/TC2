class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # move sliding window and find the max_list, i.e., naive approach
        max_list = list()
        if nums == list():
            return max_list
        else:
            window = nums[:k]
            first_max = max(window)
            max_list.append(first_max)
            
            for i in range(len(nums)-k):
                if max_list[i] <= nums[k+i]:
                    max_list.append(nums[k+i])
                else:# the code runs slow due to this part. refer to JK's code which use the 0'th element in the current window so that the code runs much faster
                    max_list.append(max(nums[i+1:k+i+1]))
                        
            return max_list