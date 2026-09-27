class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        numFresh = 0
        q = collections.deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r,c))
                
                elif grid[r][c] == 1:
                    numFresh += 1


        numMins = 0
        while numFresh > 0 and q:
            numMins += 1
            for _ in range(len(q)):
                rotR, rotC = q.popleft()
                visited.add((rotR, rotC))
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = rotR + dr, rotC + dc
                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        numFresh -= 1

                    
        return numMins if numFresh == 0 else -1
                

