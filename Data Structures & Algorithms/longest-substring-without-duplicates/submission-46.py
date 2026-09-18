class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                length = r - l + 1
                longest = max(length, longest)
            
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                
                charSet.add(s[r])
                length = r - l + 1
                longest = max(length, longest)

        return longest