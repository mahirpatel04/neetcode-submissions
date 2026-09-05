class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p, s) for p, s in zip(position, speed)], key=lambda x: x[0], reverse=True)

        stack = []

        for p, s in cars:
            time = (target - p) / s
            if not stack:
                stack.append(time)

            elif stack[-1] < time:
                stack.append(time)



        return len(stack)


