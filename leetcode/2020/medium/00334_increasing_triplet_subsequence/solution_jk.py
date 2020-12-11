class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        queue = [nums[0]]
        
        for num in nums[1:]:
            if num < queue[0]:
                queue[0] = num
            elif num > queue[-1]:
                if len(queue) == 2:
                    return True
                queue.append(num)            
            elif queue[0] < num < queue[-1]:
                queue[-1] = num            
        
        return False
        
        '''
        - The better solution
        
        first_num = float('inf')
        second_num = float('inf')
        
        for n in nums:
            if n < first_num:
                first_num = n
            elif first_num < n < second_num:
                second_num = n
            elif second_num < n:
                return True
            
        return False
        '''
        
