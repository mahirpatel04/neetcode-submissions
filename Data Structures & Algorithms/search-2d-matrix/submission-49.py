class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix) * len(matrix[0])) - 1
        while l <= r:
            m = (l + r) // 2
            outer = m // len(matrix[0])
            inner = m % len(matrix[0])

            middle_val = matrix[outer][inner]

            if middle_val == target:
                return True
            
            elif middle_val < target:
                l = m + 1
            
            elif middle_val > target:
                r = m - 1
            
        return False