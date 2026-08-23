class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = heights[0]

        # Stores currently extending heights:
        stack = []
        for i, h in enumerate(heights):
            # If segment can no longer be extended because we found a heigh that is less than the height of the segment
            if stack and stack[-1][1] > h:
                while stack and stack[-1][1] > h:
                    j, h2 = stack.pop()
                    area = (i-j) * h2
                    maxArea = max(area, maxArea)

                stack.append([j, h])
            
            else:
                stack.append([i, h])


        for i, h in stack:
            area = (len(heights) - i) * h
            maxArea = max(area, maxArea)

        return maxArea
            