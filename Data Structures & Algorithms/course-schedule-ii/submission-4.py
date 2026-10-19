class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        depMap = defaultdict(list)

        outDegrees = [0] * numCourses
        for cls, pre in prerequisites:
            depMap[pre].append(cls)
            outDegrees[cls] += 1


        q = collections.deque([c for c in range(numCourses) if outDegrees[c] == 0])

        res = []

        while q:
            cls = q.popleft()
            res.append(cls)
            for availableClass in depMap[cls]:
                outDegrees[availableClass] -= 1
                if outDegrees[availableClass] == 0:
                    q.append(availableClass)

        return res if len(res) == numCourses else []
