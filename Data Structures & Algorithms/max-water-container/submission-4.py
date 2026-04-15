class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = float("-inf")
        
        l = 0
        r = len(heights) - 1
        
        while l < r:
            area = max(area, min(heights[l], heights[r]) * (r-l))
            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1

        return area





        # for i in range(len(heights)):
        #     r = len(heights) - 1
        #     while i < r:
        #         area = max(min(heights[i], heights[r]) * (r - i), area)
        #         r -= 1

        # return area
