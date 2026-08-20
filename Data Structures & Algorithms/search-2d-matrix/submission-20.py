class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1

        while l <= r:
            mid = l + (r - l) // 2
            outer = int(mid // len(matrix[0]))
            inner = int(mid % len(matrix[0]))
            mid_val = matrix[outer][inner]

            if mid_val < target:
                l = mid + 1
            
            elif mid_val > target:
                r = mid - 1

            else:
                return True

        return False


