class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # entire sequence is sorted
            if nums[l] <= nums[r]:
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1

            # left side is sorted
            elif nums[l] <= nums[m]:
                # target belongs in left side if it is between l and m
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1






                