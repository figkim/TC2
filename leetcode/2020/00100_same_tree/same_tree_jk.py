# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        queue = []
        
        if p or q:
            queue = [(p, q)]
        
        while queue:
            node_p, node_q = queue.pop()
            
            if not (node_p and node_q):
                return False
            
            elif node_p.val != node_q.val:
                return False            
            
            if node_p.left or node_q.left:
                queue.append((node_p.left, node_q.left))
                
            if node_p.right or node_q.right:
                queue.append((node_p.right, node_q.right))
                
                
        return True
