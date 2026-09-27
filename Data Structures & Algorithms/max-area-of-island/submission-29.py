class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c):
            q = collections.deque([(r, c)])
            area = 1
            grid[r][c] = 0
            while q:
                row, col = q.popleft()
                for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS) and (0 <= nc < COLS) and (grid[nr][nc] == 1):
                        grid[nr][nc] = 0
                        q.append((nr, nc))
                        area += 1

            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea