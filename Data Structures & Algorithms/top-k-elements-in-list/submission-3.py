class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]

        for val, count in counts.items():
            freq[count].append(val)

        res = []
        for f in freq[::-1]:
            for element in f:
                res.append(element)
                if len(res) == k:
                    return res

