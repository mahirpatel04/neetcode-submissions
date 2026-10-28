class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        MOD = 10**9 + 7

        adj = [[] for _ in range(n)]
        for a, b, t in roads:
            adj[a].append((t, b))
            adj[b].append((t, a))


        minHeap = [(0, 0)]
        pathCounts = [0] * n
        pathCounts[0] = 1
        minCost = [float("inf")] * n

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            for neiCost, nei in adj[node]:
                if neiCost + cost < minCost[nei]:
                    minCost[nei] = neiCost + cost
                    pathCounts[nei] = pathCounts[node]
                    heapq.heappush(minHeap, (minCost[nei], nei))
                
                elif neiCost + cost == minCost[nei]:
                    pathCounts[nei] = (pathCounts[nei] + pathCounts[node]) % MOD

        return pathCounts[n-1]