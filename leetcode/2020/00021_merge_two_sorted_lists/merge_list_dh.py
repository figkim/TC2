# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
            
        l1_ptr, l2_ptr = l1, l2
        if l1.val < l2.val:
            newlist = ListNode(l1.val)
            l1_ptr = l1_ptr.next
        else:
            newlist = ListNode(l2.val)
            l2_ptr = l2_ptr.next
        newlist_ptr = newlist
        
        while (l1_ptr) and (l2_ptr):
            if l1_ptr.val < l2_ptr.val: 
                newlist_ptr.next = ListNode(l1_ptr.val)
                l1_ptr = l1_ptr.next
            else: 
                newlist_ptr.next = ListNode(l2_ptr.val)
                l2_ptr = l2_ptr.next
            newlist_ptr = newlist_ptr.next
        if l1_ptr:
            newlist_ptr.next = l1_ptr
        elif l2_ptr:
            newlist_ptr.next = l2_ptr
        return newlist
