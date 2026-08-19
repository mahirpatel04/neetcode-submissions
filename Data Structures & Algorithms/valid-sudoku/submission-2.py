class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            row_vals = set()
            col_vals = set()
            for j, e in enumerate(row):
                if (e != ".") and (e in row_vals):
                    return False
                else:
                    row_vals.add(e)

                if board[j][i] != "." and board[j][i] in col_vals:
                    return False
                else:
                    col_vals.add(board[j][i])


        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid_vals = set()
                for offset_i in range(3):
                    for offset_j in range(3):
                        element = board[i+offset_i][j+offset_j]
                        if element != "." and element in grid_vals:
                            return False

                        else:
                            grid_vals.add(element)





        return True


