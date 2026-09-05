class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            prev = i
            while stack and stack[-1][1] >= h:
                j, h2 = stack.pop()
                area = h2 * (i - j)
                maxArea = max(area, maxArea)
                prev = j

            stack.append((prev, h))
            
        
        print(stack)
        for i, h in stack:
            area = h * (len(heights) - i)
            maxArea = max(area, maxArea)

        return maxArea