class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for n, c in counts.items():
            buckets[c - 1].append(n)


        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for value in buckets[i]:
                res.append(value)
                if len(res) == k:
                    return res

