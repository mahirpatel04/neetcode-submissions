class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL = height[l]
        maxR = height[r]

        rain = 0
        while l < r:
            if maxL <= maxR:
                rain += maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])
            
            else:
                rain += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])

        return rain