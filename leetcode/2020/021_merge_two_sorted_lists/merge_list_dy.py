# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
        if not l1 or not l2:
            return l1 if not l2 else l2
        
        startNode = None
        currentNode = None
        rank = [l1, l2]
        
        while True:
            if rank[0].val <= rank[1].val:
                rank = [rank[0], rank[1]]
            else:
                rank = [rank[1], rank[0]]
                
            if currentNode is None:
                startNode = rank[0]
                currentNode = startNode
            else:
                currentNode.next = rank[0]
                currentNode = currentNode.next
            
            if rank[0].next is None:
                currentNode.next = rank[1]
                break
            rank[0] = rank[0].next

