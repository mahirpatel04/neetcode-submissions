class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best = r
        while l <= r:
            mid = l + (r-l)//2

            num = 0
            for p in piles:
                num += p // mid

                if p % mid != 0:
                    num += 1

            if h >= num:
                best = mid
                r = mid - 1
            elif h < num:
                l = mid + 1
            

            print(mid, num)

        return best

