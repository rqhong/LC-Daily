# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next
        
        prev, cur = None, slow
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = prev
            prev = tmp
        
        r = float("-inf")
        while prev:
            r = max(r, head.val+prev.val)
            head = head.next
            prev = prev.next
        return r