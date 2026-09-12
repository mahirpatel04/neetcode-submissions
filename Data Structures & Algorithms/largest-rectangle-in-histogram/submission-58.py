class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h))

            else:
                j = i
                while stack and stack[-1][1] >= h:
                    j, prev = stack.pop()
                    maxArea = max(maxArea, prev * (i - j))

                stack.append((j, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea