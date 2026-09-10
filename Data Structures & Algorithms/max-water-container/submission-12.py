class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # int array heights
        # two bars = container
        # want to know max amount of water that can be stored

        # widest width
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1

        return max_area