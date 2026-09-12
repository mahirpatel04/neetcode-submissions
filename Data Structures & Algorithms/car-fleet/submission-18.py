class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)

        count = 0
        prevTime = 0
        for p, s in cars:
            time = (target - p) / s
            if count != 0:
                if prevTime >= time:
                    continue
            
            count += 1
            prevTime = time


        return count