class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for n, c in counts.items():
            buckets[c - 1].append(n)

        
        res = []
        for bucket in buckets[::-1]:
            while bucket:
                res.append(bucket.pop())
                if len(res) == k:
                    return res
            