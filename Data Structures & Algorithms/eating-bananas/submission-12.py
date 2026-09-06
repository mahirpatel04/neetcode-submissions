class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            hrs = 0
            c = r + (l - r)//2
            for p in piles:
                time = math.ceil(p / c)
                hrs += time

            if hrs <= h:
                r = c - 1
                speed = min(speed, c)
            else:
                l = c + 1

        return speed
        
        

        

