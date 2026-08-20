class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        combined = sorted([(p, s) for p,s in zip(position, speed)], key=lambda x: x[0], reverse=True)
        prevTime = 0
        count = 0
        for car in combined:
            time = float((target-car[0]) / car[1])

            if time > prevTime:
                count += 1
                prevTime = time
               

        return count
