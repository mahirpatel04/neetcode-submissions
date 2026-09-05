class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [-1] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                j, temp = stack.pop()
                res[j] = i - j
                
            stack.append((i, t))

        for i, t in stack:
            res[i] = 0

        return res