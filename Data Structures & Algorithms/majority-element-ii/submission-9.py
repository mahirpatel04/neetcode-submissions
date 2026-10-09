class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        minRequired = len(nums) // 3

        res = set()
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            if counts[n] > minRequired:
                res.add(n)

        return list(res)