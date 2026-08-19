class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for num, count in counts.items():
            buckets[count - 1].append(num)

        res = []
        for b in buckets[::-1]:
            for n in b:
                res.append(n)
                if len(res) == k:
                    return res