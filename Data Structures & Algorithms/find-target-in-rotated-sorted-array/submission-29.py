class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            elif nums[m] > nums[r]:
                # start of array is to the right
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                # start of array is to the left
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                
                else:
                    r = m - 1

        return -1
