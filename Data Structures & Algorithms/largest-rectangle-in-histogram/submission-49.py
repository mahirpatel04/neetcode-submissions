class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                j, h2 = stack.pop()
                area = h2 * (i - j)
                maxArea = max(area, maxArea)
                start = j

            stack.append((start, h))
            
    
        for i, h in stack:
            
            maxArea = max(h * (len(heights) - i), maxArea)

        return maxArea