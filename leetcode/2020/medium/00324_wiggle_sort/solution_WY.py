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
            c = list()
            for i in range(len(a)):
                c.append(a[i])
                c.append(b[i])
            for i,cc in enumerate(c):
                nums[i] = cc
        elif length % 2 == 0 and nums[length//2 - 1] == nums[length//2]:
            a, b = nums[:length//2], nums[length//2:]
            c = list()
            for i in range(len(a)):
                c.append(b[i])
                c.append(a[i])
            for i,cc in enumerate(c):
                nums[i] = cc
            nums.reverse()
        elif length % 2 != 0 and nums[length//2 - 1] != nums[length//2]:
            a, b = nums[:length//2 + 1], nums[length//2 + 1:]
            c = list()
            for i in range(len(a)-1):
                c.append(a[i])
                c.append(b[i])
            c.append(a[-1])
            for i,cc in enumerate(c):
                nums[i] = cc
        else:
            a, b = nums[:length//2 + 1], nums[length//2 + 1:]
            c = list()
            for i in range(len(a)-1):
                c.append(a[i])
                c.append(b[i])
            c.append(a[-1])
            for i,cc in enumerate(c):
                nums[i] = cc

# TO DO:
# build in-place code
# code cleansing