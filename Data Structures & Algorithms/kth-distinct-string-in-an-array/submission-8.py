class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map = {}
        seen = set()
        for i, a in enumerate(arr):
            if a in map:
                seen.add(a)
                del map[a]

            elif a not in seen:
                map[a] = i

        if len(map.keys()) < k:
            return ""
        
        else:
            return list(map.keys())[k-1]
            