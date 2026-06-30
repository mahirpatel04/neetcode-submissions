class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}
        for s_char, t_char in zip(s, t):
            s_count[s_char] = s_count.get(s_char, 0) + 1
            t_count[t_char] = t_count.get(t_char, 0) + 1

        return s_count == t_count