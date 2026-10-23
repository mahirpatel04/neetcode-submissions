class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visit = [False] * n

        def dfs(i):
    
            for nei in adjList[i]:
                if visit[nei] == False:
                    visit[nei] = True
                    dfs(nei)

        num = 0
        for i in range(n):
            if visit[i] == False:
                visit[i] = True
                dfs(i)
                num += 1

        for v in visit:
            if v == False:
                num += 1

        return num
