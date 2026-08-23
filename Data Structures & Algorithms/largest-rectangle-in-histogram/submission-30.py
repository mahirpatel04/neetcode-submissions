class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = heights[0]
        stack = []

        for i, h in enumerate(heights):
            if stack and h < stack[-1][1]:
                # Po
                while stack and stack[-1][1] >= h:
                    j, prev_h = stack.pop()
                    area = (i - j) * prev_h
                    maxArea = max(maxArea, area)
                
                stack.append([j, h])

            else:
                stack.append([i, h])

        while stack:
            k, remaining_h = stack.pop()
            area = (len(heights) - k) * remaining_h
            maxArea = max(maxArea, area)

        return maxArea