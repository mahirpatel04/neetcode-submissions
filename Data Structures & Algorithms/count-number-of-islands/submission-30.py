class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        numIslands = 0

        def dfs(r, c):
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS) or grid[r][c] == "0" or (r,c) in visited:
                return

            visited.add((r,c))
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row = dr + r
                col = dc + c
                dfs(row, col)




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    numIslands += 1
                


        return numIslands