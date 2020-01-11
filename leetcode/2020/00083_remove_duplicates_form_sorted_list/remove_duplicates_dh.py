# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        ptr1, ptr2 = head, head.next
        while ptr2:
            if ptr1.val != ptr2.val:
                ptr1 = ptr2
                ptr2 = ptr2.next
            else:
                ptr2 = ptr2.next
                ptr1.next = ptr2
        return head


