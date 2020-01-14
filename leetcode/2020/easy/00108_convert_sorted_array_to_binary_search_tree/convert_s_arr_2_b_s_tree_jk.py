# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        middle = len(nums)//2

        num = nums[middle]
        left_nums = nums[:middle]
        right_nums = nums[middle+1:]
                
        node = TreeNode(num)        

        node.left = self.sortedArrayToBST(left_nums)
        node.right = self.sortedArrayToBST(right_nums)

        return node
        
        
