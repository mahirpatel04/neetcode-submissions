class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        reverse = sorted([(p, s) for p,s in zip(position, speed)], key=lambda x: x[0], reverse=True)

        stack = []


        # for each car 
        for i, car in enumerate(reverse):
            time = (target - car[0])/car[1]
            # if stack is empty we can simply add the current car into the stack
            if len(stack) == 0:
                # time is distance needed to travel divided by speed
                stack.append((car, time))

            # if stack not empty we have to check with top of stack and only add it in if it reached AFTER (in more time)
            elif time > stack[-1][1]:
                    stack.append((car, time))
    
                


        return len(stack)