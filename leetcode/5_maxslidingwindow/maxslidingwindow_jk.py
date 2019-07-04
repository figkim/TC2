class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        if N == 0:
            return []
        if k == 1:
            return nums

        max_num = max(nums[:k])
        max_list = [max_num]

        for i in range(k, N):
            if max_num < nums[i]:
                max_num = nums[i]

            elif max_num == nums[i-k]:
                max_num = max(nums[i-k+1:i+1])

            max_list.append(max_num)

        return max_list
