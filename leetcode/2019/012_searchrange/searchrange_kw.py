class Solution:
    def searchRange(self, nums, target):
        def whileSearch(start, end, mode):
            out = -1
            while start <= end:  # equal !!
                mid = int((start + end) / 2)
                mid_value = nums[mid]
                if mid_value > target:
                    end = mid - 1
                elif mid_value < target:
                    start = mid + 1
                elif mid_value == target:
                    if mode == "left":
                        out = mid
                        end = mid - 1
                    elif mode == "right":
                        out = mid
                        start = mid + 1
            return out

        start = 0
        end = len(nums) - 1
        lm = whileSearch(start, end, mode="left")  # find the leftmost index
        rm = whileSearch(start, end, mode="right")  # find the leftmost index
        return [lm, rm]