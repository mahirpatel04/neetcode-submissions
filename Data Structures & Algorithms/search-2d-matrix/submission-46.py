class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0])

        while l <= r and l < len(matrix) * len(matrix[0]):
            m = int((l + r) / 2)
            outer = int(m // len(matrix[0]))
            inner = int(m % len(matrix[0]))
            mid_val = matrix[outer][inner]
            print(l, r, outer, inner, mid_val)

            if mid_val < target:
                l = m + 1
            
            elif mid_val > target:
                r = m - 1

            else:
                return True

        return False
