# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        
        queue = [(root, root.val-1)]
        
        while queue:
            node, max_val = queue.pop()
            
            if node.val >= max_val:
                cnt += 1
                max_val = node.val
                
            if node.left is not None:
                queue.append((node.left, max_val))
                
            if node.right is not None:
                queue.append((node.right, max_val))
                
                
        return cnt
