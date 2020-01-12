# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        if not (root.left or root.right):
            return 1
        
        queue = [(root, 1)]        
        max_depth = 1
        
        while queue:
            node, depth = queue.pop()
            
            if node.left:
                queue.append((node.left, depth+1))
                max_depth = max(max_depth, depth+1)
                
            if node.right:
                queue.append((node.right, depth+1))
                max_depth = max(max_depth, depth+1)
                
        return max_depth
