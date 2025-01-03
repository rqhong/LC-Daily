# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head: return head
        prev = head
        cur = head.next
        prev_head = prev
        cur_head  = cur        

        # total len is odd
        while(prev and cur):
            if not cur.next:
                break
            prev.next = cur.next
            prev = prev.next
            cur.next = prev.next
            cur = cur.next
            
        prev.next = cur_head

        return prev_head
