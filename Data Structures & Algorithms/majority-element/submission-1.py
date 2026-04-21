class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        return sorted([(c, n) for n, c in counts.items()], key=lambda x: x[0], reverse=True)[0][1]