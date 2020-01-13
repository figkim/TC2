# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = [(root, 1)]
        
        while queue:
            node, lvl = queue.pop(0)
            
            if not (node.left or node.right):
                return lvl
            
            if node.left:
                queue.append((node.left, lvl+1))
                
            if node.right:
                queue.append((node.right, lvl+1))
                
        return -1
