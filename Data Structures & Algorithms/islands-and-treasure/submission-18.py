class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        q = collections.deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == INF and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))


            dist += 1