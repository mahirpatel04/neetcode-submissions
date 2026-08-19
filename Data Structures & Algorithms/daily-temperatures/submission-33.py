class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if stack:
                while stack and t > stack[-1][1]:
                    res[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                
                stack.append([i, t])

            else:
                stack.append([i, t])
        
        return res


            