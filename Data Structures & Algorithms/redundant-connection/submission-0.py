class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # graph stores the edges we have already added so far
        graph = defaultdict(list)

        def has_path(src, target, visited):
            # If we reached the target, there is already a path
            if src == target:
                return True

            visited.add(src)

            # Try visiting all neighbours of src
            for nei in graph[src]:
                if nei not in visited:
                    if has_path(nei, target, visited):
                        return True

            # No path found from src to target
            return False

        for a, b in edges:
            # Before adding edge [a, b], check if a and b
            # are already connected in the current graph.
            #
            # If yes, adding this edge creates a cycle.
            if has_path(a, b, set()):
                return [a, b]

            # If no path exists yet, safely add the edge.
            graph[a].append(b)
            graph[b].append(a)