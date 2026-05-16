class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_map = { i : [] for i in range(n)}
        for a,b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)

        components = 0
        visited = set()

        def dfs(node):
            visited.add(node)

            for neighbour in adj_map[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components