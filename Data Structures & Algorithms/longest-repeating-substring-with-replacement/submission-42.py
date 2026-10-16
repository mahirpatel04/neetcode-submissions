class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxF = 0
        counts = {}
        longest = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxF = max(maxF, counts[s[r]])

            while r - l + 1 > maxF + k:
                counts[s[l]] -= 1
                l += 1
            
            longest = max(r - l + 1, longest)

        return longest