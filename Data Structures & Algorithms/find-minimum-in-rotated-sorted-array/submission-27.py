class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        minVal = nums[0]

        # 4, 0, 1, 2, 3

        # 2, 3, 4, 0, 1

        while l < r - 1:
            m = (l + r) // 2
            minVal = min(minVal, nums[m])

            if nums[l] > nums[m] and nums[m] < nums[r]:
                r = m

            else:
                l = m
        

        return min(minVal, nums[l], nums[r])