class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        # # largest value we have seen so far on either side
        # maxL = height[l]
        # maxR = height[r]

        # water = 0
        # while l < r:
        #     if maxL < maxR:
        #         l += 1
        #         maxL = max(maxL, height[l])
        #         water += maxL - height[l]
        #     else:
        #         r -=1
        #         maxR = max(maxR, height[r])
        #         water += maxR - height[r]

        
        # return water


        maxLeft = []
        L = height[0]
        for h in height:
            if L >= h:
                maxLeft.append(L)
            else:
                L = h
                maxLeft.append(h)
        
        maxRight = []
        R = height[-1]
        for h in height[::-1]:
            if R >= h:
                maxRight.append(R)
            else:
                R = h
                maxRight.append(h)
        maxRight = maxRight[::-1]

        print(maxLeft)
        print(maxRight)

        water = 0
        for i in range(len(maxLeft)):
            water += min(maxLeft[i], maxRight[i]) - height[i] 

        return water

