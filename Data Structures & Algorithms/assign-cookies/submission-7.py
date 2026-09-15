class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gP, sP = 0, 0
        while sP < len(s) and gP < len(g):
            if g[gP] <= s[sP]:
                gP += 1

            sP += 1


        return gP