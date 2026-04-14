class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffMap = {}

        for i, n in enumerate(nums):
            if n in diffMap:
                return [diffMap[n], i]

            else:
                diffMap[target - n] = i

        
