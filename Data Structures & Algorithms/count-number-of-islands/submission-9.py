class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0
        #visited = set()
        

        def bfs(r, c):
            q = collections.deque()
            #visited.add((r, c))
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r2 = row + dr
                    c2 = col + dc
                    if r2 in range(rows) and c2 in range(cols) and grid[r2][c2] == "1":
                        #visited.add((r2, c2))
                        grid[r2][c2] = "0"
                        q.append((r2, c2))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    numIslands += 1

        return numIslands
