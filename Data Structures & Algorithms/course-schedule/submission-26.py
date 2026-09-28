class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        outDegrees = [0 for i in range(numCourses)]
        dependencyMap = defaultdict(list)
        for crs, pre in prerequisites:
            outDegrees[crs] += 1
            dependencyMap[pre].append(crs)

        
        q = collections.deque([crs for crs in range(numCourses) if outDegrees[crs] == 0])
        finish = 0
        while q:
            pre = q.popleft()
            finish += 1
            for crs in dependencyMap[pre]:
                outDegrees[crs] -= 1
                if outDegrees[crs] == 0:
                    q.append(crs)

        return finish == numCourses

                    

        