class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p, s) for p, s in zip(position, speed)], key = lambda x: x[0], reverse=True)

        fleetTimes = []
        numFleets = 0
        for p, s in cars:
            carTime = (target - p) / s

            if (not fleetTimes) or (carTime > fleetTimes[-1]):
                fleetTimes.append(carTime)
                numFleets += 1
        
        return numFleets