class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        total = 0
        def dfs(i, total, combination):
            if total == target:
                res.append(combination.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            combination.append(nums[i])
            dfs(i, total + nums[i], combination)
            combination.pop()
            dfs(i + 1, total, combination)

        
        dfs(0, 0, [])
        return res

