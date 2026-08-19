class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = 1
        post_prod = 1

        res = [1] * len(nums)

        for i, n in enumerate(nums):
            res[i] = pre_prod
            pre_prod *= n

        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post_prod
            post_prod *= nums[i]

        return res

