class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffMap = {}

        # for each element in nums
        for i, n in enumerate(nums):

            # if the element is already a complement (adds up to target) to another number we saw previously then just return that
            if n in diffMap:
                return [diffMap[n], i]

            else:
                # store the complement we need and the index of the original element
                diffMap[target - n] = i

        
