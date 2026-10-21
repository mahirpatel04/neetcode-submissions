class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maxSoFar = nums[0]
        minSoFar = nums[0]
        res = maxSoFar

        for i in range(1, len(nums)):
            n = nums[i]
            tempMax = max(n, maxSoFar * n, minSoFar * n)
            minSoFar = min(n, maxSoFar * n, minSoFar * n)
            maxSoFar = tempMax

            res = max(maxSoFar, res)

        return res