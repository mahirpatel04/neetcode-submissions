class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            # while there's things to pop and the curr temp is greater than the top of the stack
            while stack and t > stack[-1][0]:
                last_t, last_i = stack.pop()
                res[last_i] = i - last_i
                
            # once we've popped everything we can we add in the current temperature into the stack to wait
            stack.append((t, i))

        return res
