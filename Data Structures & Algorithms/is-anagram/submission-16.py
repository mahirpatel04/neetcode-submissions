class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for sChar, tChar in zip(s, t):
            s_map[sChar] += 1
            t_map[tChar] += 1

        return s_map == t_map