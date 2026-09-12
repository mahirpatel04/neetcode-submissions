class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_area = 0
        while l < r:
            if heights[l] < heights[r]:
                max_area = max(heights[l] * (r - l), max_area)
                l += 1
            else:
                max_area = max(heights[r] * (r - l), max_area)
                r -= 1

        return max_area