class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = 0
        length = 0

        for r in range(len(s)):
            if s[r] in map:
                l = max(l, map[s[r]] + 1)


            map[s[r]] = r
            length = max(length, r -l + 1)

        return length