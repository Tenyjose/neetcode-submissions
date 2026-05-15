class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(row,col):
            grid[row][col] = 0
            total = 1

            for dr,dc in directions:
                new_row = row+dr
                new_col = col+dc

                if 0<= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    total += dfs(new_row,new_col)

            return total



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max(area,dfs(row,col))

        return area
