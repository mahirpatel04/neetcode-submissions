class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}
        for i, n in enumerate(nums):
            if target - n in seenMap:
                return [seenMap[target-n], i]

            else:
                seenMap[n] = i

    
