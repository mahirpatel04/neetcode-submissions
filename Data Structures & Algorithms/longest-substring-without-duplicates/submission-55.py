class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        longest = 0
        mapping = {}
        for r in range(len(s)):
            if s[r] in mapping:
                l = max(l, mapping[s[r]] + 1)
            
            mapping[s[r]] = r
            longest = max(r - l + 1, longest)

        return longest
