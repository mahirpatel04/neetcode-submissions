class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        nums.sort()
        while i < len(nums) - 2:
            if nums[i] > 0:
                return res

            if i > 1 and nums[i] == nums[i - 1]:
                i += 1
                continue

            
            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    lst = [nums[i], nums[l], nums[r]]
                    if lst not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

        
            i += 1

        return res