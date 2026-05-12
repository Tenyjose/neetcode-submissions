# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0

        dummy = ListNode(0)
        curr = dummy

        while curr1 or curr2 or carry:
            if curr1:
                val1 = curr1.val 
            else:
                val1 = 0

            if curr2:
                val2 = curr2.val
            else:
                val2 = 0

            total = val1+val2+carry
            carry = total // 10
            digit  = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next

        return dummy.next
