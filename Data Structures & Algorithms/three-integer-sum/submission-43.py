class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break

            # skip all the duplicates for the first number
            if i > 0 and n == nums[i - 1]:
                continue

            # set 2 ptrs one next to the first num and one at the end of the array
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = n + nums[l] + nums[r]
                if sum == 0:
                    # put the result in
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # shift the left pointer as far in while seeing duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                
                elif sum < 0:
                    l += 1
                
                else:
                    r -= 1

        return res