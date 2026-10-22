class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeList = [[] for _ in range(n)]
        for a, b in edges:
            edgeList[a].append(b)
            edgeList[b].append(a)

        visit = [False] * n


        def dfs(i):
            for nei in edgeList[i]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        

        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        
        return res
