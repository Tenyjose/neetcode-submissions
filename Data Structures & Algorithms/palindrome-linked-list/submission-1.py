# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = deque()

        curr = head

        while curr:
            queue.append(curr.val)
            curr=curr.next

        while len(queue)>1:
            if queue.popleft() != queue.pop():
                return False

        return True
            