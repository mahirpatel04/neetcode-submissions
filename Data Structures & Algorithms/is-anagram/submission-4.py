class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        s_map, t_map = {}, {}
        for s_char, t_char in zip(s, t):
            s_map[s_char] = s_map.get(s_char, 0) + 1
            t_map[t_char] = t_map.get(t_char, 0) + 1

        print(s_map, t_map)
        return s_map == t_map