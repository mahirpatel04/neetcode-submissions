class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, combination, total):
            if total == target:
                res.append(combination.copy())
                return

            elif i >= len(nums) or total > target:
                return

            combination.append(nums[i])
            backtrack(i, combination.copy(), total + nums[i])
            combination.pop()
            backtrack(i + 1, combination.copy(), total)


        backtrack(0, [], 0)
        return res