class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        counts = [0] * 26
        for c in s1:
            counts[ord(c) - ord('a')] += 1

        idealWL = len(s1)
        l = 0
        windowCounts = [0] * 26
        for r in range(len(s2)):
            length = r - l + 1
            if length > idealWL:
                windowCounts[ord(s2[l]) - ord('a')] -= 1
                l += 1

            windowCounts[ord(s2[r]) - ord('a')] += 1
            if windowCounts == counts:
                return True

        return False





