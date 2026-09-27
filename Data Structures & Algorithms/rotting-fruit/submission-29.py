class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        numFresh = 0
        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                
                elif grid[r][c] == 1:
                    numFresh += 1

        numMins = 0
        while q and numFresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS) and (0 <= nc < COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        numFresh -= 1
            
            numMins += 1

        return numMins if numFresh == 0 else -1
