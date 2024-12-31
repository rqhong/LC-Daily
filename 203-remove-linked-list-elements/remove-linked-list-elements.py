# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        while head:
            if head.val == val:
                head = head.next
            else:
                break
        else:
            return head
        
        node = head

        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
                
        
        return head