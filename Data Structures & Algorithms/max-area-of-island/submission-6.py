class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0
        

        def bfs(r, c):
            q = collections.deque()
            grid[r][c] = 0
            q.append((r, c))

            area = 0

            while q:
                area += 1
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r2 = row + dr
                    c2 = col + dc
                    if r2 in range(rows) and c2 in range(cols) and grid[r2][c2] == 1:
                        
                        grid[r2][c2] = 0
                        q.append((r2, c2))


            return area


        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    numIslands += 1
                    maxArea = max(area, maxArea)

        return maxArea