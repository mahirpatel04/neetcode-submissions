class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first time pass we will multiply 

        pre = [1] * len(nums)
        post = [1] * len(nums)


        pre_product = 1
        for i in range(len(nums)-1, -1, -1):
            pre[i] = pre_product
            pre_product *= nums[i]



        post_product = 1
        for i in range(len(nums)):
            post[i] = post_product
            post_product *= nums[i]


        return [pre_val * post_val for pre_val, post_val in zip(pre,post)]


