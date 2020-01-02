class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        if (len(nums) == 0) or (nums[0] > target) or (nums[-1] < target):
            return [-1, -1]
        
        elif len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        
        else:
            n, exp = len(nums), 1
            
            while n/(2**(exp)) > 0:
                exp += 1
            
            left, right = 0, n-1
            while nums[left] <= target <= nums[right]:
                print left, right
                center = (left+right)/2
                
                if nums[center] < target:
                    left = center+1
                    if nums[right] > target:
                        right -= 1
                elif nums[center] > target:
                    right = center-1
                    if nums[left] < target:
                        left += 1
                else:
                    k, l = 0, 0
                    while (center-k >= 0) and (nums[center-k] == target):
                        k += 1
                    while (center+l < n) and (nums[center+l] == target):
                        l += 1
                    if (nums[center-k+1] != target) or (nums[center+l-1] != target):
                        return [-1, -1]
                    else:
                        return [center-k+1,center+l-1]

            return [-1, -1]
        '''   
        if (len(nums) == 0) or (nums[0] > target) or (nums[-1] < target):
            return [-1, -1]
        
        else:
            n, exp = len(nums), 1
            
            while n/(2**(exp)) > 0:
                exp += 1
            
            left, right = 0, n-1
            while (nums[left] <= target <= nums[right]) and (left <= right):
                center = (left+right)/2
                if nums[center] < target:
                    left = center+1
                else:
                    break
            while (nums[left] <= target <= nums[right]) and (left <= right):
                center = (left+right)/2
                if nums[center] > target:
                    right = center-1
                else:
                    break
            
            while nums[left] < target:
                left += 1
            while nums[right] > target:
                right -= 1
            
            if (left > right) or (nums[left] != target) or (nums[right] != target):
                return [-1, -1]
            else:
                return [left, right]
        '''   
        if (len(nums) == 0) or (nums[0] > target) or (nums[-1] < target):
            return [-1, -1]
        
        else:
            exp = 1
            
            while len(nums)/(2**(exp)) > 0:
                exp += 1
            
            left, right = 0, len(nums)-1
            while (nums[left] <= target <= nums[right]) and (left <= right):
                center = (left+right)/2
                if nums[center] < target:
                    left = center+1
                elif nums[center] > target:
                    right = center-1
                else:
                    break
            
            while nums[left] < target:
                left += 1
            while nums[right] > target:
                right -= 1
            
            if (nums[left] != target) or (nums[right] != target) or (left > right):
                return [-1, -1]
            else:
                return [left, right]
        '''