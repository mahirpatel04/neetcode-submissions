class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        minVal = nums[0]

        # 4, 0, 1, 2, 3

        # 2, 3, 4, 0, 1

        while l < r:
            m = (l + r) // 2
            minVal = min(minVal, nums[m])

            if nums[r] > nums[m]:
                r = m

            else:
                l = m + 1
        

        return nums[l]