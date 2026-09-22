class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        longest = 0
        for r in range(len(s)):
            if s[r] in charSet:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                
            charSet.add(s[r])
            longest = max(r - l + 1, longest)

        return longest