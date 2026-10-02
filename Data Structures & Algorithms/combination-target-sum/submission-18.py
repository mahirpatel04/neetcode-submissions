class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(combination, i, total):
            if total == target:
                res.append(combination.copy())
                return

            if i >= len(nums) or total > target:
                return


            combination.append(nums[i])
            backtrack(combination, i, total + nums[i])
            combination.pop()
            backtrack(combination, i + 1, total)

        backtrack([], 0, 0)

        return res