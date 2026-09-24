class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 2, 3, 4, 5 3

        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                start, prevH = stack.pop()
                area =  prevH * (i - start)
                maxArea = max(area, maxArea)
                
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea