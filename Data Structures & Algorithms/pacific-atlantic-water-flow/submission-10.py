class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific, atlantic = set(), set()


        # water flows from all cells in left column and top row to the pacific 
        # and water flows all bottom rows and right column to the atlantic
        # so a better approach would be to move from the ocean and perfom a dfs
        # So when we start from an ocean border, we can move to a neighbour only 
        # if the neighbour height is greater than or equal to the current height.

        def dfs(r,c,visited,prevHeight):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r,c) in visited or
                heights[r][c] < prevHeight):
                return

            visited.add((r,c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, visited, heights[r][c])


        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atlantic,heights[rows-1][c])

        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atlantic,heights[r][cols-1])


        return list(pacific & atlantic)

        