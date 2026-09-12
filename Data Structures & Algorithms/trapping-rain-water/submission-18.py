class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        for h in height:
            water += min(leftMax, rightMax) - h

            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
            
            else:
                r -= 1
                rightMax = max(rightMax, height[r])


        return water