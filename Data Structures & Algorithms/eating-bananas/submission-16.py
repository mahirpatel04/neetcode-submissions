class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = r

        while l <= r:
            hrs = 0
            c = l + (r - l)//2
            for p in piles:
                time = math.ceil(p / c)
                hrs += time

            if hrs <= h:
                r = c - 1
                speed = c
            else:
                l = c + 1

        return speed
        
        

        

