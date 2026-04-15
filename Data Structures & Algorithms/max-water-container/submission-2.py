class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = float("-inf")
        
        

        for i in range(len(heights)):
            r = len(heights) - 1
            while i < r:
                area = max(min(heights[i], heights[r]) * (r - i), area)
                r -= 1

        return area
