# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        queue = [root]
        
        while queue:
            node = queue.pop()
            
            if not node:
                continue
            
            if abs(self.get_height(node.left) - self.get_height(node.right)) > 1:
                return False
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
                
        return True
        
        
    def get_height(self, node):
        if not node:
            return 0
        
        return max(self.get_height(node.left), self.get_height(node.right)) + 1
