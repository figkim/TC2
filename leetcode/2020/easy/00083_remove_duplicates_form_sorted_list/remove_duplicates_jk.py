# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        
        while node is not None:
            val = node.val
            next_node = node.next
            while next_node is not None and next_node.val == val:
                next_node = next_node.next
                
            node.next = next_node
            
            node = next_node
            
        return head
