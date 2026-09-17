class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_set = set(t)
        new = [(i, c) for i, c in enumerate(s) if c in t_set]

        # Window answer details:
        length = float("inf")
        start, end = 0, 0

        # Count:
        counts = {}
        for c in t:
            counts[c] = counts.get(c, 0) + 1

        required_matches = len(counts)

        # Window details:
        l, r = 0, 0
        windowCounts = {}
        formed = 0
        while r < len(new):
            character = new[r][1]
            windowCounts[character] = windowCounts.get(character, 0) + 1

            if character in counts:
                if windowCounts[character] == counts[character]:
                    formed += 1

                while l <= r and formed == required_matches:
                    character = new[l][1]

                    end_window = new[r][0]
                    start_window = new[l][0]
                    if end_window - start_window + 1 < length:
                        end = end_window
                        start = start_window
                        length = end_window - start_window + 1
                    
                    windowCounts[character] -= 1
                    if windowCounts[character] < counts[character]:
                        formed -= 1
                    l += 1

            r += 1


        if length == float("inf"):
            return ""
        
        else:
            return s[start:end + 1]