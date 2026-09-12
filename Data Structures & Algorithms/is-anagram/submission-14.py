class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCounts = {}
        tCounts = {}

        for sChar, tChar in zip(s,t):
            sCounts[sChar] = sCounts.get(sChar, 0) + 1
            tCounts[tChar] = tCounts.get(tChar, 0) + 1

        return sCounts == tCounts