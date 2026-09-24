class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        water = 0
        for i in range(len(height)):
            if leftMax < rightMax:
                water += leftMax - height[i]
                l += 1
                leftMax = max(leftMax, height[l])
            
            else:
                water += rightMax - height[i]
                r -= 1
                rightMax = max(rightMax, height[r])

        return water
            