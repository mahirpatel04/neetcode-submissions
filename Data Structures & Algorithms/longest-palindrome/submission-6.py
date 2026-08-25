class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1

        count = 0
        odd = False
        for char, num in counts.items():
            if num % 2 == 0:
                count += num
            else:
                odd = True
                count += num - 1


        return count + 1 if odd else count
            