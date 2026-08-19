class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i - 1] == n:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r] + n
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        
        return res