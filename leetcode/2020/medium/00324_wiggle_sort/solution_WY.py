class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums.sort()
        if length % 2 == 0 and nums[length//2 - 1] != nums[length//2]:
            a, b = nums[:length//2], nums[length//2:]
            for i in range(len(a)):
                nums[2*i] = a[i]
                nums[2*i+1] = b[i]
        elif length % 2 == 0 and nums[length//2 - 1] == nums[length//2]:
            a, b = nums[:length//2], nums[length//2:]
            for i in range(len(a)):
                nums[2*i] = b[i]
                nums[2*i+1] = a[i]
            nums.reverse()
        else:
            a, b = nums[:length//2 + 1], nums[length//2 + 1:]
            for i in range(len(a)-1):
                nums[2*i] = a[i]
                nums[2*i+1] = b[i]
            nums[-1] = a[-1]

# TO DO:
# build in-place code w/ constant extra space -> do not use variable a, b
# build linear time code -> sort() used in the current code
# code cleansing