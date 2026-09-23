class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for i, n in enumerate(nums):
            if target - n in diffMap:
                return [diffMap[target - n], i]
            else:
                diffMap[n] = i
        
        return []