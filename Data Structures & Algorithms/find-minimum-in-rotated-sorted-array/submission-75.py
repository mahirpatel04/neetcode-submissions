class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = nums[l]
        while l <= r:
            m = (l + r) // 2

            minVal = min(minVal, nums[m])
            # left half sorted which means lowest will be in unsorted section to the right
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return minVal