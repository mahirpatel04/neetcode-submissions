class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = [[False for _ in range(COLS)] for _ in range(ROWS)]
        atlantic = [[False for _ in range(COLS)] for _ in range(ROWS)]
        pacQ = collections.deque()
        atlQ = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacQ.append((r, c))
                    pacific[r][c] = True
            
                if r == ROWS - 1 or c == COLS - 1:
                    atlQ.append((r, c))
                    atlantic[r][c] = True

        while pacQ:
            r, c = pacQ.popleft()
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS) and (0 <= nc < COLS) and pacific[nr][nc] != True and heights[nr][nc] >= heights[r][c]:
                    pacific[nr][nc] = True
                    pacQ.append((nr, nc))


        while atlQ:
            r, c = atlQ.popleft()
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS) and (0 <= nc < COLS) and atlantic[nr][nc] != True and heights[nr][nc] >= heights[r][c]:
                    atlantic[nr][nc] = True
                    atlQ.append((nr, nc))

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])

        return res


