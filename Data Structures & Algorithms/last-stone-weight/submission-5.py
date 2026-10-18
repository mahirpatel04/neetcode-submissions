class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)



        while len(heap) > 1:
            first = -1 * heapq.heappop(heap)
            second = -1 * heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -1 * abs(first - second))

        print(heap)

        return -1 * heap[0] if heap else 0