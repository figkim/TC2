# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            tmp = []
            t_queue = queue[:]
            queue = []
            
            for node in t_queue:
                tmp.append(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                
            result.append(tmp)
                
        return reversed(result)
