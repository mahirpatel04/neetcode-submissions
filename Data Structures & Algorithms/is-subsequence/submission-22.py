class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a, b = 0, 0

        while a < len(s) and b < len(t):
            # found next match
            if s[a] == t[b]:
                a += 1
                b += 1

            # skip/delete a character
            else:
                b += 1
        
        return a == len(s)