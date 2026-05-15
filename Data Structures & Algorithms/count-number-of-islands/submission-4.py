class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        Rows = len(grid)
        Cols = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(row,col):
            grid[row][col] = "0"
            for dr,dc in directions:
                nr = row+dr
                nc = col+dc

                if 0<= nr < Rows and 0<=nc<Cols and grid[nr][nc] == "1":
                    dfs(nr,nc)

        for row in range(Rows):
            for col in range(Cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row,col)

        return islands
