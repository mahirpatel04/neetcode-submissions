class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we want to expand our window to length of s1
        # windowLengthIdeal = len(s1)
        # i = 0
        # while i < len(s2):
        #     # get the start of s1 first        
        #     ideal = 0
        #     if s2[i] != s1[0]:
        #         i += 1
        #         continue

        #     # first expand the window as far right as possible
        #     for r in range(i, i + windowLengthIdeal):
        #         if r < len(s2) and s2[r] == s1[r - i]:
        #             ideal += 1
        #         else:
        #             break

        #     # then expand the window as far left the remaining leftOver amount
        #     leftOver = windowLengthIdeal - ideal

        #     print("DEBUG", leftOver)
        #     for l in range(i - 1, i - 1 - leftOver, -1):
        #         if l >= 0 and s2[l] == s1[-1 * l + i - 1 - leftOver + windowLengthIdeal]:
        #             ideal += 1
            

        #     if ideal == windowLengthIdeal:
        #         return True

        #     i += 1

        # return False
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





