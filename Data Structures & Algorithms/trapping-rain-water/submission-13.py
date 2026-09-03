class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        maxL = height[l]
        maxR = height[r]

        rain = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                rain += maxL - height[l]
            
            else:
                r -= 1
                maxR = max(maxR, height[r])
                rain += maxR - height[r]

        return rain