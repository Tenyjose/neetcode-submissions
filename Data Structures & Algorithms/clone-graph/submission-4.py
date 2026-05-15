"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        OldToNew = {}
        
        def dfs (node):

            if node in OldToNew:
                return OldToNew[node]

            copy = Node(node.val)

            OldToNew[node] = copy


            for neighbour in node.neighbors:
                    cloned_neighbour = dfs(neighbour)
                    copy.neighbors.append(cloned_neighbour)

            return copy

        return dfs(node) if node else None