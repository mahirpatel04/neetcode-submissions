class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = nums[l]
        while l <= r:
            m = (l + r) // 2

            minVal = min(minVal, nums[m])

            if nums[m] >= nums[r]:
                l = m + 1
            
            else:
                r = m - 1


        return minVal