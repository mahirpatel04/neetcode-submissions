class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        combined = sorted([(p, s) for p,s in zip(position, speed)], key=lambda x: x[0], reverse=True)
        stack = []
        for car in combined:
            time = float((target-car[0]) / car[1])

            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)                

        return len(stack)
