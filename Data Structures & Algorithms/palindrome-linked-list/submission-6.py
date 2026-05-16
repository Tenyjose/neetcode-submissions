# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # when it finishes the slow pointers would be at the middle and the fast pointer would
        # be at the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now we can reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left,right = head , prev
        while left and right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
        
            