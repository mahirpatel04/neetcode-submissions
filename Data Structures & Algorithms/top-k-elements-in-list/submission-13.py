class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        

        buckets = [[] for i in range(len(nums))]

        for n, c in counts.items():
            buckets[c - 1].append(n)

        res = []
        for b in buckets[::-1]:
            for n in b:
                res.append(n)
                if len(res) == k:
                    return res