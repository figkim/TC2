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
        queue = [(root, 1)]
        
        tmp = []
        c_lvl = 1
        
        while queue:
            node, lvl = queue.pop(0)
            if lvl == c_lvl:
                tmp.append(node.val)
            else:
                result.append(tmp)
                tmp = [node.val]
                c_lvl = lvl
                
            if node.left:
                queue.append((node.left, lvl+1))
                
            if node.right:
                queue.append((node.right, lvl+1))
                
        result.append(tmp)
                
        return reversed(result)
