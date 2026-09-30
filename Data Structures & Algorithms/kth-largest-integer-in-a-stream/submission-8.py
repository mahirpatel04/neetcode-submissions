class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        stack = []
        for i in range(self.k):
            stack.append(heapq.heappop(self.heap))

        target = stack[-1]
        for s in stack:
            heapq.heappush(self.heap, s)

        return -target

        
        
