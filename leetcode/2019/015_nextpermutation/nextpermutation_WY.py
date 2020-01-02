class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) != 1:
            boolean = False
            for i in range(len(nums)-1,0,-1):
                if nums[i-1] < nums[i]:
                    boolean = True
                    break

            if boolean:
                part = nums[i-1:]
                first = min([x for x in part[1:] if x > part[0]])
                part.pop(part.index(first))
                temp = [first]
                part.sort()
                temp.extend(part)
                nums[i-1:] = temp
            else:
                nums[::] = nums[::-1]

        else:
            pass