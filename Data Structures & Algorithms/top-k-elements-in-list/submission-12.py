class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create n different buckets
        buckets = [[] for i in range(len(nums))]

        # Count all the number of appearances for each of the numbers in the sequence
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        # For each of the numebrs place them in the correct bucket determined by the count.
        # ie: if 3 shows up 5 times in nums then put it in index 4 bucket
        for num, count in counts.items():
            buckets[count - 1].append(num)

        # iterate through the buckets in reverse order
        # keep adding elements on the result until we have enough
        res = []
        for b in buckets[::-1]:
            for n in b:
                res.append(n)
                if len(res) == k:
                    return res