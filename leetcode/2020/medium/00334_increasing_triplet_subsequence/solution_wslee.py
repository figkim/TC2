class Solution:
    def increasingTriplet(self, nums):
        first = float('inf')  # first smallest num
        second = float('inf')  # second smallest num

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                # num is bigger than both first and second (smallest) numbers
                return True
            # print(first, second, num)

        return False

