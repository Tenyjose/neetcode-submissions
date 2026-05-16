class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        #visited = set()

        # dfs fuction
        def dfs(r,c):

            if (r < 0 or r>= rows or
            c < 0 or c >= cols or
            board[r][c] != "O" ): # (r,c) in visited or):
                return

            board[r][c] = "T"

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                dfs(nr,nc)

        # first we get the top and bottom rows
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            if board[rows-1][c] == "O":
                dfs(rows-1,c)


        # to get the first and last columns
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)


        # so now we have a set that hiols the points "O" that are 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"