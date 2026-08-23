class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        # Stores currently extending heights:
        stack = []
        for i, h in enumerate(heights):
            # If segment can no longer be extended because we found a heigh that is less than the height of the segment
            start = i
            while stack and stack[-1][1] >= h:
                j, h2 = stack.pop()
                area = (i-j) * h2
                maxArea = max(area, maxArea)
                start = j

            stack.append([start, h])


        for i, h in stack:
            maxArea = max((n - i) * h, maxArea)

        return maxArea
            