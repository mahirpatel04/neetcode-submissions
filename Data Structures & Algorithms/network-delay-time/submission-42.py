class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n + 1)]
        for src, dst, time in times:
            edges[src].append((time, dst))

        pq = [(0, k)]
        visited = set()
        final = -1
        while pq:
            time, node = heapq.heappop(pq)
            if node not in visited:
                final = time
                visited.add(node)
                for t, d in edges[node]:
                    if d not in visited:
                        heapq.heappush(pq, (time + t, d))


        
        return final if len(visited) == n else -1
