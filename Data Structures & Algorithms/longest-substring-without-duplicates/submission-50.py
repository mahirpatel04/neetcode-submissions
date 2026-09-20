class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        mapping = {}
        
        for r in range(len(s)):
            if s[r] in mapping:
                l = max(mapping[s[r]] + 1, l)
            
            mapping[s[r]] = r
            longest = max(r - l + 1, longest)

        return longest