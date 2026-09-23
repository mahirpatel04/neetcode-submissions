class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}
        for sChar, tChar in zip(s, t):
            sCount[sChar] = sCount.get(sChar, 0) + 1
            tCount[tChar] = tCount.get(tChar, 0) + 1

        return sCount == tCount
    