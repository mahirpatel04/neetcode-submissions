class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxVal = 0
        for n in nums:
            count = 0
            if n - 1 not in s:
                while n in s:
                    count += 1
                    n += 1
            
            maxVal = max(count, maxVal)

        return maxVal