class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            q = collections.deque((r, c))
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            area = 1
            for dr, dc in directions:
                row, col = dr + r, dc + c
                area += bfs(row, col)

            return area




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxArea = max(area, maxArea)

        return maxArea

