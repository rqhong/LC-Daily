# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def calculate(l):
            mul = 1
            total = 0
            while l:
                n = l.val
                total += n * mul
                mul *= 10
                l = l.next
            return total
        
        num1 = calculate(l1)
        num2 = calculate(l2)
        total = num1 + num2
        res = []

        if total == 0:
            return ListNode(0)

        head = ListNode(total % 10)
        total //= 10  
        curr = head

        while total > 0:
            curr.next = ListNode(total % 10)
            curr = curr.next
            total //= 10  

        return head