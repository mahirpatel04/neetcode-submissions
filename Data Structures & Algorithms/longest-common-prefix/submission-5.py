class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        currPref = strs[0]
        for s in strs:
            while currPref:
                if s.startswith(currPref):
                    currPref = currPref
                    break
                else:
                    currPref = currPref[:-1]

        return currPref
