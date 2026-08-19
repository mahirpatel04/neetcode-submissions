class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = defaultdict(list)

        for s in strs:
            tup = [0] * 26
            for c in s:
                tup[ord(c) - ord('a')] += 1

            map[tuple(tup)].append(s)

        return list(map.values())