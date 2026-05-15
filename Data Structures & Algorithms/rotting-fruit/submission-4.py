class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        queue = deque()
        ROWS,COLS = len(grid),len(grid[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        # getting the fresh count and adding the rotten tomatoes to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        time = 0
        while queue and count>0:
            for _  in range(len(queue)):	
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr , c+dc
                    if 0<= nr <ROWS and 0<= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        count -= 1
                        queue.append((nr,nc))

            time += 1

        return time if count == 0 else -1
        