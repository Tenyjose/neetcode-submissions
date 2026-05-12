"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OldToNew = {}
        if not head:
            return None

        # First pass creating the hashmap cloning the nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            OldToNew[curr] = copy
            curr = curr.next

        # Pass 2:  set next and random using hashmap
        curr = head
        while curr:
            if curr.next:
                OldToNew[curr].next = OldToNew[curr.next]
            if curr.random:
                OldToNew[curr].random = OldToNew[curr.random]
            curr = curr.next

        return OldToNew[head]
