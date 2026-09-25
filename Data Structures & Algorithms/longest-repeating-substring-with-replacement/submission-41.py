class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        counts = {}
        longest = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxf = max(counts[s[r]], maxf)

            while r - l + 1 - maxf > k:
                counts[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            
        return longest
            
            