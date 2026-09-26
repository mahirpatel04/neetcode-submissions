class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS) or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            area = 1
            for dr, dc in directions:
                row, col = dr + r, dc + c
                area += dfs(row, col)

            return area




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxArea = max(area, maxArea)

        return maxArea

