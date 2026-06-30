class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        print(arr)
        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for n, c in counts.items():
            arr[c].append(n)

        res = []
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
            if len(res) == k:
                return res

        