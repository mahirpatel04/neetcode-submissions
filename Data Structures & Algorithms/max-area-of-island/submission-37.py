class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0

            area = 1
            grid[r][c] = 0
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)
            
            return area
                
        

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(dfs(r, c), area)

        return area