class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)

        stack = []
        count = 0
        for p, s in cars:
            time = (target - p) / s
            if stack:
                if stack[-1] >= time:
                    continue
            
            stack.append(time)
            count += 1


        return count