class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        maxf = 0
        l = 0
        res = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxf = max(maxf, counts[s[r]])

            # number to replace
            if r - l + 1 - maxf <= k:
                res = max(res, r - l + 1)
            else:
                counts[s[l]] -= 1
                l += 1

        return res