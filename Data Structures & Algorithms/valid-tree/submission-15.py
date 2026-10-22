class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        edgeList = [[] for _ in range(n)]
        for a, b in edges:
            edgeList[a].append(b)
            edgeList[b].append(a)

        print(edgeList)
        visited = set([0])
        q = collections.deque([(0, -1)])
        while q:
            node, parent = q.popleft()
            for nei in edgeList[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                q.append((nei, node))
                visited.add(nei)

        return len(visited) == n



            


        return True