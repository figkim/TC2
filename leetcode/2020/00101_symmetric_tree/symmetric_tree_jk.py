# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        if not (root.left or root.right):
            return True
        
        queue = [(root.left, root.right)]
        
        while queue:
            node_left, node_right = queue.pop()
            
            if not (node_left and node_right):
                return False
            if node_left.val != node_right.val:
                return False
            
            if node_left.left or node_right.right:
                queue.append((node_left.left, node_right.right))
                
            if node_left.right or node_right.left:
                queue.append((node_left.right, node_right.left))
                
                
        return True
            
