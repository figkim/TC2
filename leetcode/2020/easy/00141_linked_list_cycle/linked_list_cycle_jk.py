# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head
        
        while True:
            if not (slow and slow.next and fast.next and fast.next.next):
                return False
            
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                return True  
