class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                leftSide = s[l:r]
                rightSide = s[l+1:r+1]
                return leftSide == leftSide[::-1] or rightSide == rightSide[::-1]

            l += 1
            r -= 1

        return True