# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    hash = set()
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        if head in self.hash:
            return True
        
        self.hash.add(head)
        
        return self.hasCycle(head.next)
