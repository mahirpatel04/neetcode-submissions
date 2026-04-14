class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first time pass we will multiply 

        res = [1] * len(nums)
 
        pre_product = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = pre_product
            pre_product *= nums[i]


        post_product = 1
        for i in range(len(nums)):
            res[i] *= post_product
            post_product *= nums[i]


        return res


