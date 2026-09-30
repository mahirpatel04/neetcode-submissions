class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = defaultdict(list)
        for src, dest, time in times:
            edges[src].append((dest, time))

        
        minHeap = [(0, k)]
        visited = set()
        t = 0

        while minHeap:
            time, src = heapq.heappop(minHeap)
            if src in visited:
                continue
            
            visited.add(src)
            t = time

            for neighbor, time in edges[src]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (time + t, neighbor))

        return t if len(visited) == n else -1 




