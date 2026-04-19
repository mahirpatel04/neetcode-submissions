class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            print(stack, i, t)
            while stack:
                last_t, last_i = stack[-1]
                if t > last_t:
                    stack.pop()
                    res[last_i] = i - last_i
                
                else:
                    break
                

            stack.append((t, i))

        return res
