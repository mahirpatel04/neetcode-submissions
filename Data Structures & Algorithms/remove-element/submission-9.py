class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        original = len(nums)
        while val in nums:
            nums.remove(val)
        
        return len(nums)