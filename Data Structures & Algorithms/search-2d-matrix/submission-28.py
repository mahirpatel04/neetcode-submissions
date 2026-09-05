class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        l, r = 0, (len(matrix) * len(matrix[0])) - 1

        while l <= r:
            c = r + (l - r) // 2

            obj = matrix[c//len(matrix[0])][c%len(matrix[0])]
            if obj > target:
                r = c - 1

            elif obj < target:
                l = c + 1

            else:
                return True

        return False