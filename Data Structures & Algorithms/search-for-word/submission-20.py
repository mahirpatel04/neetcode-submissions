class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i, visited):
            if i == len(word):
                return True
            
            if (r < 0 or r == ROWS) or (c < 0 or c == COLS) or (r, c) in visited or board[r][c] != word[i]:
                return
            
            visited.add((r, c))
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1, visited):
                    return True

            visited.remove((r, c))
            return False
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True

        return False

