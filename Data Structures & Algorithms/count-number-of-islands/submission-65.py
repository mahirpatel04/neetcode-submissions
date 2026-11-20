class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr, nc)
            

        numIslands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    numIslands += 1


        return numIslands
