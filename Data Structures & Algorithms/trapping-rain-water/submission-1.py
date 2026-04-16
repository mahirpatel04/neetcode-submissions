class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0: return 0
        

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        amt = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                amt += leftMax - height[l]
            
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                amt += rightMax - height[r]
    
        return amt

