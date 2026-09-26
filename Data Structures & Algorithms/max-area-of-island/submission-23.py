class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS) or grid[r][c] == 0:
                return 0

            area = 1
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    if (row + dr, col + dc) not in visited:
                        area += bfs(row + dr, col + dc)

            return area




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxArea = max(area, maxArea)

        return maxArea

