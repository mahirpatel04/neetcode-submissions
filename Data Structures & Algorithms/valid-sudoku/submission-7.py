class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        ROWS, COLS = 9, 9

        for i in range(ROWS):
            for j in range(COLS):
                num = board[i][j]

                if num == ".":
                    continue

                if num in rows[i] or num in cols[j] or num in grids[(i//3, j//3)]:
                    return False

                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    grids[(i//3, j//3)].add(num)

        return True
