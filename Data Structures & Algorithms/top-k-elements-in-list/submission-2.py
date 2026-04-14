class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        maxHeap = [(-1 * v, k) for k, v in counts.items()]
        heapq.heapify(maxHeap)
        # for k, v in counts.items():
        #     heapq.heappush(maxHeap, (-1*v, k))

        print(maxHeap)

        return [heapq.heappop(maxHeap)[1] for i in range(k)]